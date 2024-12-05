from django.urls import path

from main.apps import MainConfig
from main.views import (
    index,
    contact,
    mission,
    history,
    DoctorListView,
    DoctorDetailView,
    ServicesListView,
    ServicesDetailView,
    first_page,
    finalize_appointment,
    HistoryAppointmentView,
    DoctorCreateView,
    DoctorDeleteView, ServicesCreateView, ServicesDeleteView, AppointmentDeleteView,
)

app_name = MainConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("mission/", mission, name="mission"),
    path("history/", history, name="history"),
    path("doctor/list", DoctorListView.as_view(), name="doctor_list"),
    path("doctor/create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("doctor/view/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    path("doctor/delete/<int:pk>/", DoctorDeleteView.as_view(), name="doctor_delete"),
    path("services/create/", ServicesCreateView.as_view(), name="services_create"),
    path("services/list", ServicesListView.as_view(), name="services_list"),
    path(
        "services/view/<int:pk>/", ServicesDetailView.as_view(), name="services_detail"
    ),
    path("services/delete/<int:pk>/", ServicesDeleteView.as_view(), name="services_delete"),
    path("appointment/create/", first_page, name="create_appointment"),
    path("appointment/delete/<int:pk>/", AppointmentDeleteView.as_view(), name="appointment_delete"),
    path("appointment/finalize/", finalize_appointment, name="finalize_appointment"),
    path(
        "appointment/history/",
        HistoryAppointmentView.as_view(),
        name="history_appointment",
    ),
]
