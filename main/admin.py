from django.contrib import admin
from main.models import Doctor, Services, Appointment


@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "specialization")


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ("title", "doctor", "price")


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ("services", "doctor", "date", "time")
