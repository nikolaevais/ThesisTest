from django.contrib import admin
from main.models import Doctor, Services, Appointment, Info, Results


@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "specialization")


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ("id", "title", "doctor", "price")


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ("id", "services", "doctor", "date", "time")


@admin.register(Results)
class Result(admin.ModelAdmin):
    list_display = ("id", "title", "description")