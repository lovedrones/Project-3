from django.urls import path
from . import views


urlpatterns = [
    #
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('patients/', views.patients_index, name='index'),
    path('patients/<str:patient_name>', views.patients_detail, name='detail'),
    path('registration/', views.registration_signup, name='signup'),
]