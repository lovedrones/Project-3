from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Patient

# Create your views here.



def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def patients_detail(request, patient_name):
    patient = item for item in Patient if Patient.get('name')==patient_name
    return render(request, 'patients/details.html', {'patients' : patients})
def patients_index(request):
    patients = Patient.objects.filter(user = request.user) 
    return render(request, 'patients/index.html', { 'patients' : patients } )
def registration_signup(request):
    return render(request, 'registration/signup.html') 