from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def hello_world(request):
    return render(request, 'base.html', {'greeting': 'hello world'})


@login_required
def users(request):
    all_permissions = Permission.objects.all
    result = []
    for user in User.objects.all():
        result.append((user, Permission.objects.filter(user=user)))
    return render(request, 'users.html', {'all_permissions': all_permissions, 'result': result})
