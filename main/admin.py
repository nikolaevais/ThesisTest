from django.contrib import admin
from main.models import Doctor


@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "specialization")
