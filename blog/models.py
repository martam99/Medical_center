from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    photo = models.ImageField(upload_to='blog/', verbose_name='photo')

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
