from django.conf.urls import url
from user_management_web import views
from django.contrib.auth import views as auth_views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^$', views.main_control),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^users$', views.users, name='users'),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^recruiterPage', views.recruiter_page, name='recruiter_page'),
    url(r'^leadPage', views.lead_page, name='lead_page'),
    url(r'^recruiterPage', views.recruiter_page, name='recruiter_page'),
    url(r'^superUserPage', views.super_user_page, name='super_user_page'),

]
