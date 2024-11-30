from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Doctor, Services


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


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
