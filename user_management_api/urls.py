from django.conf.urls import url
from user_management_api import views

urlpatterns = [
    url(r'^hello_world$', views.hello_world)
    ]
