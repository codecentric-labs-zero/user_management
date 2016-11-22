from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rolepermissions.shortcuts import get_user_role


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_role(self):
        if self.user.is_superuser:
            return 'Superuser'
        return get_user_role(self.user).__str__(self)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
