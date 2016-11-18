from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include('user_management_web.urls')),
    url(r'^api/', include('user_management_api.urls'))
]
