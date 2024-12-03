from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", **NULLABLE)
    tg_name = models.CharField(max_length=20, verbose_name="Телеграмм", **NULLABLE)
    avatar = models.ImageField(upload_to="users/avatar/", verbose_name="Аватар", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def get_display_name(self):
        return self.email
