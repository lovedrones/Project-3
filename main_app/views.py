from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Pills, Appointments, Patient
from .forms import PatientForm
# Create your views here.



def home(request):
      return render(request, 'home.html')
# Updated from login to login_user

#   Patients index, and detail views
def patients_index(request):
  patients = Patient.objects.filter(user=request.user)
  return render(request, 'patients/index.html', { 'patients': patients })

def patients_detail(request, patient_name):
    patient = Patient.objects.get(name=patient_name)
    return render(request, 'patients/details.html', { 'patient': patient})

# Pills create, update, and delete views

class PillsCreate(CreateView):
    model = Pills
    fields = ['name', 'total', 'pil_days', 'dosage'] 
    def form_valid(self, form):
        return super().form_valid(form)

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
# class PatientsCreate(CreateView):
#   model = Patient
#   fields = '__all__'
#   success_url = '/patients/create/'

    
class PatientsUpdate(UpdateView):
    model = Patient
    fields = '__all__'

class PatientsDelete(DeleteView):
    model = Patient
    success_url = '/patients/'

# signup views
def signup(request):
  print('hi')
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
  print('hi')
  return render(request, 'registration/signup.html', context)




def patients_create(request):
    print(request.user)
    if request.method == 'POST':
        patient = Patient(user = request.user)
        form = PatientForm(request.POST , instance=patient)
        print(form)
        if form.is_valid():
            patient.save()
            print('---------------------Form Validated')
            return redirect('index')
        else:
            print('---------------------Form Denied')
            return redirect('index')
    elif request.method == 'GET':
        return render(request, 'patients/create.html')

