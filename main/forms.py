from django import forms
from django.forms import ModelForm, BooleanField

from main.models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = ["services", "doctor", "date", "time"]
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
