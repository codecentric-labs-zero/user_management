from django.conf.urls import url
from user_management_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^$', views.hello_world),
    ]
