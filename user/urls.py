from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import UserCreate, UserUpdate

app_name = UserConfig.name

urlpatterns = [
    path('create/', UserCreate.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
