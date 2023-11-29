from django.urls import path

from main.apps import MainConfig
from main.views import SiteTemplate, home, info, sending

app_name = MainConfig.name

urlpatterns = [
    path('', SiteTemplate.as_view(), name='base'),
    path('about_us/', home, name='home'),
    path('info/', info, name='info'),
    path('sending/', sending, name='sending'),
]
