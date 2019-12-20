from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_index, name='index'),
    path('patients/', views.patients_details, name='details'),
    path('registration/', views.registration_signup, name='signup'),
]