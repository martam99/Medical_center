from django.shortcuts import render
from django.views.generic import DetailView, ListView

from medcenter.models import Services, Doctors


# Create your views here.
class ServicesDetailView(DetailView):
    model = Services
    template_name = 'medcenter/service_detail.html'


class ServicesListView(ListView):
    model = Services
    template_name = 'medcenter/service_list.html'


class DoctorsDetailView(DetailView):
    model = Doctors
    template_name = 'medcenter/doctors_detail.html'


