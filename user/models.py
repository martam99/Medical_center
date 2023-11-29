from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.CharField(max_length=150, verbose_name='почта', unique=True)
    phone = models.CharField(verbose_name='номер телефона', **NULLABLE)
    fullname = models.CharField(max_length=150, verbose_name='ФИО')
    is_active = models.BooleanField(default=True, verbose_name='activity')

    objects = BaseUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
