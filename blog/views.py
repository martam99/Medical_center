from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Blog


# Create your views here.
class BlogView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
