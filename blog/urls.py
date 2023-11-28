from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogListView

app_name = BlogConfig.name
urlpatterns = [
    path('blog/<int:pk>/', BlogView.as_view(), name='blog_view'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
]
