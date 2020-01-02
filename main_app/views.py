from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pills, Appointments, Patient

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')
# Updated from login to login_user
def login_user(request):
    return render(request, 'login.html')
def patients_details(request):
    return render(request, 'patients/details.html')
def patients_index(request):
    return render(request, 'patients/index.html')
def registration_signup(request):
    return render(request, 'registration/signup.html')


#   Patients index, and detail views
def patients_index(request):
#   patients = Patient.objects.filter(user=request.user)
  return render(request, 'patients/index.html', { 'patients': patients })

def patients_detail(request, patient_id):
#   patient = Patient.objects.get(id=patient_id)
  return render(request, 'patient/detail.html')

# Pills create, update, and delete views
class PillsCreate(CreateView):
  model = Pills
  fields = '__all__'
  success_url = '/patients/'

class PillsUpdate(UpdateView):
    model = Pills
    fields = '__all__'

class PillsDelete(DeleteView):
    model = Pills
    success_url = '/patients/'

# Appointments create, update, and delete views
class AppointmentsCreate(CreateView):
  model = Appointments
  fields = '__all__'
  success_url = '/patients/'

class AppointmentsUpdate(UpdateView):
    model = Appointments
    fields = '__all__'

class AppointmentsDelete(DeleteView):
    model = Appointments
    success_url = '/patients/'

# Patient create, update, and delete views
class PatientsCreate(CreateView):
  model = Patient
  fields = '__all__'
  success_url = '/patients/'

class PatientsUpdate(UpdateView):
    model = Patient
    fields = '__all__'

class PatientsDelete(DeleteView):
    model = Patient
    success_url = '/patients/'

# signup views
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)