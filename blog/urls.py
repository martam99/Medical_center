from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView

app_name = BlogConfig.name
urlpatterns = [
    path('blog/<int:pk>/', BlogView.as_view(), name='blog_view')
]
