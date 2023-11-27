from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog
from medcenter.models import Services, Doctors


# Create your views here.
class SiteTemplate(TemplateView):
    template_name = 'main/general.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_list'] = Blog.objects.order_by('?')[:2]
        context_data['service_list'] = Services.objects.all
        context_data['doctor_list'] = Doctors.objects.all
        return context_data

