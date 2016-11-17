from django.conf.urls import url
from user_management_web import views
from django.contrib.auth import views as auth_views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^$', views.hello_world),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^users$', views.users, name='users'),
    ]
