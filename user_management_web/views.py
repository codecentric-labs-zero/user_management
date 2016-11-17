from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def hello_world(request):
    return render(request, 'base.html', {'greeting': 'hello world'})


@login_required
def users(request):
    return render(request, 'users.html', {'users': User.objects.all()})
