from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, DoctorListView, DoctorDetailView, ServicesListView, ServicesDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('doctor/list', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/view/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('services/list', ServicesListView.as_view(), name='services_list'),
    path('services/view/<int:pk>/', ServicesDetailView.as_view(), name='services_detail'),

]
