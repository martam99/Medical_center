# Generated by Django 4.2.7 on 2023-11-27 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 27, 10, 18, 35, 890203), verbose_name='дата публикации'),
        ),
    ]
