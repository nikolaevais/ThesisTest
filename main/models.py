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
    job_title = models.CharField(max_length=100, verbose_name="Должность")

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname} ({self.specialization})"


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name='Тело письма')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Доктор")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    photo = models.ImageField(upload_to="main/services/photo/", verbose_name="Фото", **NULLABLE)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"{self.title} {self.price}"


class Appointment(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуги")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Доктор")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.services} {self.date} {self.time}"
