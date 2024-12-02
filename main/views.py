from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from datetime import datetime, timedelta

from main.forms import AppointmentForm
from main.models import Doctor, Services, Appointment


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

    return render(request, 'main/contact.html')


def first_page(request):
    all_time = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")
    max_day_value = (yesterday + timedelta(days=14)).strftime("%Y-%m-%d")

    if request.GET.get('servise') is None:
        servises = Services.objects.all()
        context = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'all_time': all_time,
            'servises': servises,
            'step_1': True
        }
        return render(request, 'main/appointment_form.html', context)

    else:
        service_id = request.GET.get('servise')
        doctors = Doctor.objects.filter(services__id=service_id)
        servises = Services.objects.all()  # повторно получить услуги для второго шага
        context = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'all_time': all_time,
            'servises': servises,
            'doctors': doctors,
            'selected_service_id': service_id,
            'step_1': False,
            'step_2': True
        }
        return render(request, 'main/appointment_form.html', context)


def finalize_appointment(request):
    if request.method == 'GET':
        doctor_id = request.GET.get('doctor')
        selected_service_id = request.GET.get('servise')
        selected_date = request.GET.get('date')
        selected_time = request.GET.get('time')

        # Проверка занятости времени
        if Appointment.objects.filter(doctor_id=doctor_id, date=selected_date, time=selected_time).exists():
            return render(request, 'main/error.html',
                          {'message': 'Выбранное время занято. Пожалуйста, выберите другое время.'})

        # Сохранение записи в БД
        doctor = Doctor.objects.get(id=doctor_id)
        service = Services.objects.get(id=selected_service_id)
        appointment = Appointment.objects.create(
            doctor=doctor,
            services=service,
            date=selected_date,
            time=selected_time
        )

        # Передача информации о записи в шаблон
        return render(request, 'main/appointment_success.html', {'appointment': appointment})


class DoctorCreateView(CreateView):
    model = Doctor
    fields = ("first_name", "last_name", "surname", "specialization", "experience", "education", "avatar", "job_title")
    success_url = reverse_lazy('main:doctor_list')


class DoctorListView(ListView):
    model = Doctor


class DoctorDetailView(DetailView):
    model = Doctor


class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ("first_name", "last_name", "surname", "specialization", "experience", "education", "avatar", "job_title")
    success_url = reverse_lazy('main:doctor_list')


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('main:doctor_list')


class ServicesCreateView(CreateView):
    model = Services
    fields = ("title", "description", "surname", "doctor", "price", "photo")
    success_url = reverse_lazy('main:services_list')


class ServicesListView(ListView):
    model = Services


class ServicesDetailView(DetailView):
    model = Services


class ServicesUpdateView(UpdateView):
    model = Services
    fields = ("title", "description", "surname", "doctor", "price", "photo")
    success_url = reverse_lazy('main:services_list')

    def get_success_url(self):
        return reverse('main:services_list', args=[self.kwargs.get('pk')])


class ServicesDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy('main:services_list')

# class AppointmentCreateView(CreateView):
#     model = Appointment
#     form_class = AppointmentForm
#     success_url = reverse_lazy('main:index')
#
#
# class AppointmentListView(ListView):
#     model = Appointment
#
#
# class AppointmentDetailView(DetailView):
#     model = Appointment
#
#
# class AppointmentUpdateView(UpdateView):
#     model = Appointment
#     fields = ("services", "doctor", "date", "time")
#     success_url = reverse_lazy('main:services_list')
#
#     def get_success_url(self):
#         return reverse('main:services_list', args=[self.kwargs.get('pk')])
#
#
# class AppointmentDeleteView(DeleteView):
#     model = Appointment
#     success_url = reverse_lazy('main:services_list')
