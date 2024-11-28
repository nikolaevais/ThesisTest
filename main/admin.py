from django.contrib import admin
from main.models import Doctor, Services


@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "specialization")


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ("title", "doctor", "price")
