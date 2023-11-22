from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog


# Create your views here.
class SiteTemplate(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_list'] = Blog.objects.order_by('?')[:2]
        return context_data

