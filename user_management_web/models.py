from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rolepermissions.shortcuts import get_user_role
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


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


class Product(models.Model):
    date_of_creation = models.DateTimeField(auto_now=True, editable=False)
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return "name: " + self.product_name + " created: " + str(self.date_of_creation.date())


class ProductParts(models.Model):
    part_name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, related_name="product")


MAX_AMOUNT_PARTS_FOR_PRODUCT = 5

sparePartsFormSet = inlineformset_factory(Product, ProductParts, fields='__all__', can_delete=False,
                                          extra=MAX_AMOUNT_PARTS_FOR_PRODUCT)


class ProductAndPartsForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['date_of_creation']
        fields = ['product_name']
