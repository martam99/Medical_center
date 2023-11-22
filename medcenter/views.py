from django.shortcuts import render
from django.views.generic import DetailView, ListView

from medcenter.models import Services, Doctors


# Create your views here.
class ServicesDetailView(DetailView):
    model = Services


class ServicesListView(ListView):
    model = Doctors


class DoctorsDetailView(DetailView):
    model = Doctors
