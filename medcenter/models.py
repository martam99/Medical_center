from django.db import models


# Create your models here.
class Doctors:
    fullname = models.CharField


class Services(models.Model):
    service = models.CharField(max_length=150, verbose_name='услуги')
    content = models.TextField(verbose_name='контент')
    photo = models.ImageField(upload_to='med_services', verbose_name='изображения', default='no photo')
    doctors = models.ForeignKey(Doctors, on_delete=models.SET_NULL, verbose_name='врачи')

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
