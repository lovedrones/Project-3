from django.urls import path
from . import views


urlpatterns = [
    # Basic Urls
    path('', views.home, name='home'),
    path('login/', views.login, name='login_user'),
    path('patients/', views.patients_index, name='index'),
    path('patients/', views.patients_details, name='details'),
    path('registration/', views.registration_signup, name='signup'),

    # create,update, and delete paths for pills model
    path('pills/create/', views.PillsCreate.as_view(), name='pills_create'),
    path('pills/<int:pk>/update/', views.PillsUpdate.as_view(), name='pills_update'),
    path('pills/<int:pk>/delete/', views.PillsDelete.as_view(), name='pills_delete'),

    # create,update, and delete paths for appointments
    path('appointments/create/', views.AppointmentsCreate.as_view(), name='appointments_create'),
    path('appointments/<int:pk>/update/', views.AppointmentsUpdate.as_view(), name='appointments_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentsDelete.as_view(), name='appointments_delete'),

    # create,update, and delete paths for Patients
    path('patients/create/', views.PatientsCreate.as_view(), name='patients_create'),
    path('patients/<int:pk>/update/', views.PatientsUpdate.as_view(), name='patients_update'),
    path('patients/<int:pk>/delete/', views.PatientsDelete.as_view(), name='patients_delete'),
]