from django.urls import reverse
from django.test import TestCase

from users.forms import UserRegisterForm


class UserTest(TestCase):
    def setUp(self):
        self.user = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }

    def test_user_registration(self):
        """Тест регистрации нового пользователя."""
        response = self.client.post(reverse("users:register"), self.user)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserRegisterForm)

    def test_user_registration_without_email(self):
        """Тест регистрации без указания email."""
        data = self.user
        data["email"] = ""
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, 200)

    def test_user_registration_without_password(self):
        """Тест регистрации без указания пароля"""
        data = self.user
        data["password"] = ""
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        """Тест входа пользователя"""
        self.client.post(reverse("users:register"), self.user)

        # Теперь пробуем войти
        login_data = {"email": self.user["email"], "password": self.user["password"]}
        response = self.client.post(reverse("users:login"), login_data)
        self.assertEqual(response.status_code, 200)
