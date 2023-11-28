from django.urls import path

from medcenter.apps import MedcenterConfig
from main.views import SiteTemplate
from medcenter.views import ServicesDetailView, ServicesListView, DoctorsDetailView

app_name = MedcenterConfig.name

urlpatterns = [
    path('detail/<int:pk>/', ServicesDetailView.as_view(), name='service_detail'),
    path('list/', ServicesListView.as_view(), name='service_list'),
    path('doc_detail/<int:pk>/', DoctorsDetailView.as_view(), name='doc_detail'),
]
