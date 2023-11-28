from django.db import models

from blog.models import NULLABLE


# Create your models here.
class Doctors(models.Model):
    fullname = models.CharField(max_length=150, verbose_name='полное имя')
    mail = models.CharField(max_length=150, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='номер телефона')
    position = models.CharField(max_length=150, verbose_name='должность', **NULLABLE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'врач'
        verbose_name_plural = 'врачи'


class Services(models.Model):
    service = models.CharField(max_length=150, verbose_name='услуги')
    content = models.TextField(verbose_name='контент')
    photo = models.ImageField(upload_to='med_services', verbose_name='изображения', default='no photo')
    doctors = models.ForeignKey(Doctors, on_delete=models.SET_NULL, verbose_name='врачи', **NULLABLE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
