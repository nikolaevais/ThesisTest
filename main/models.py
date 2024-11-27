from django.db import models

from config import settings
from users.models import NULLABLE


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    surname = models.CharField(max_length=100, verbose_name="Отчество", **NULLABLE)
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    experience = models.IntegerField(verbose_name="Стаж работы")
    education = models.TextField(verbose_name="Образование")
    avatar = models.ImageField(upload_to="main/doctor/avatar/", verbose_name="Аватар", **NULLABLE)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname} ({self.specialization})"
