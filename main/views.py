from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Doctor


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


class DoctorListView(ListView):
    model = Doctor


class DoctorDetailView(DetailView):
    model = Doctor
