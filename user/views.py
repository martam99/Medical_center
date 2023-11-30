from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from user.form import UserCreation, UserUpdateForm
from user.models import User


# Create your views here

class UserCreate(CreateView):
    model = User
    form_class = UserCreation
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:login')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на нашей платформе, добро пожаловать на МарМед',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('main:base')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(DetailView):
    model = User


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('main:base')