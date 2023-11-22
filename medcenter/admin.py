from django.contrib import admin

from medcenter.models import Doctors, Services


# Register your models here.
@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'mail', 'phone')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'content', 'photo', 'doctors')
