from django.forms import ModelForm
from .models import Patient, Pills, Days, Appointments


class PatientForm(ModelForm):
  class Meta:
    model = Patient
    exclude = ('user', 'pills', 'appointments',)


class AppointmentsForm(ModelForm):
  class Meta:
    model = Appointments
    exclude = ('pills', 'appointments',)


class PatientForm(ModelForm):
  class Meta:
    model = Patient
    exclude = ('user', 'pills', 'appointments',)

