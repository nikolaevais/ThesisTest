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

    def test_doctor_delete(self):
        """Тестирование удаления докторов."""
        response = self.client.post(
            reverse("main:doctor_delete", args=[self.doctor.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Doctor.objects.filter(id=self.doctor.id).exists())


class ServicesTestCase(TestCase):
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

        self.services = Services.objects.create(
            title="УЗИ",
            description="Описание",
            doctor=self.doctor,
            price="1500.00",
        )

    def test_services_str(self):
        """Тестирование отображения строкового значения"""
        self.assertEqual(str(self.services), "УЗИ 1500.00")

    def test_services_delete(self):
        """Тестирование удаления услуги."""
        response = self.client.post(
            reverse("main:services_delete", args=[self.services.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Services.objects.filter(id=self.services.id).exists())


class AppointmentTestCase(TestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(
            first_name="Иван",
            last_name="Иванов",
            specialization="Терапевт",
            experience=10,
            education="МГУ",
            job_title="Главный врач",
        )

        self.user = User.objects.create(
            email="test@test.ru", password="testpassword"
        )

        self.services = Services.objects.create(
            title="УЗИ",
            description="Описание",
            doctor=self.doctor,
            price="1500.00",
        )

        self.appointment = Appointment.objects.create(
            services=self.services,
            doctor=self.doctor,
            date="2024-04-04",
            time="07:00",
            user=self.user
        )

    def test_appointment_str(self):
        """Тестирование отображения строкового значения"""
        self.assertEqual(str(self.appointment), "УЗИ 1500.00 2024-04-04 07:00")

    def test_appointment_delete(self):
        """Тестирование удаления записи"""
        response = self.client.post(
            reverse("main:appointment_delete", args=[self.appointment.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Appointment.objects.filter(id=self.services.id).exists())
