from django.urls import path, include
from . import views

urlpatterns = [
    # Basic Urls
    path('', views.home, name='home'),
    path('patients/', views.patients_index, name='index'),
    path('patients/<str:patient_name>', views.patients_detail, name='detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    # create,update, and delete paths for pills model
    path('pills/create/', views.PillsCreate.as_view(), name='pills_create'),
    path('pills/<int:pk>/update/', views.PillsUpdate.as_view(), name='pills_update'),
    path('pills/<int:pk>/delete/', views.PillsDelete.as_view(), name='pills_delete'),

    # create,update, and delete paths for appointments
    path('appointments/create/', views.AppointmentsCreate.as_view(), name='appointments_create'),
    path('appointments/<int:pk>/update/', views.AppointmentsUpdate.as_view(), name='appointments_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentsDelete.as_view(), name='appointments_delete'),

    # create,update, and delete paths for Patients
    path('patients/create/', views.patients_create, name='patients_create'),
    path('patients/<str:pk>/update/', views.PatientUpdate.as_view(), name='patients_update'),   
    path('patients/<str:patient_name>/delete/', views.patient_delete, name='patients_delete'),

]