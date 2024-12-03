from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, mission, history, DoctorListView, DoctorDetailView, ServicesListView, \
    ServicesDetailView, \
    first_page, finalize_appointment, HistoryAppointmentView
app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('mission/', mission, name='mission'),
    path('history/', history, name='history'),
    path('doctor/list', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/view/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('services/list', ServicesListView.as_view(), name='services_list'),
    path('services/view/<int:pk>/', ServicesDetailView.as_view(), name='services_detail'),
    path('appointment/create/', first_page, name='create_appointment'),
    path('appointment/finalize/', finalize_appointment, name='finalize_appointment'),
    path('appointment/history/', HistoryAppointmentView.as_view(), name='history_appointment'),

]
