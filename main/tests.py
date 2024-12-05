from django.urls import reverse
from django.test import TestCase

from main.models import Doctor, Services, Appointment
from users.models import User
from datetime import date, time


class DoctorTestCase(TestCase):
    def setUp(self):

        self.doctor = Doctor.objects.create(
            first_name="Иван",
            last_name="Иванов",
            surname="Иванович",
            specialization="Терапевт",
            experience=10,
            education="МГУ",
            job_title="Главный врач",
        )

    def test_doctor_str(self):
        """Тестирование отображения строкового значения"""
        self.assertEqual(str(self.doctor), "Иван Иванов Иванович (Терапевт)")

    def test_doctor_create(self):
        """Тестирование создания доктора."""
        data = {
            "first_name": "Петров",
            "last_name": "Петр",
            "surname": "Петрович",
            "specialization": "Хирургия",
            "experience": 5,
            "education": "Медицинское училище",
            "job_title": "Хирург",
        }
        response = self.client.post(reverse("main:create_doctor"), data)

        self.assertEqual(response.status_code, 302)

    def test_doctor_delete(self):
        """Тестирование удаления докторов."""
        response = self.client.post(
            reverse("main:doctor_delete", args=[self.doctor.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Doctor.objects.filter(id=self.doctor.id).exists())
