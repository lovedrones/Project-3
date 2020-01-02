from django.contrib import admin
from .models import Patient, Pills, Appointments, Days

# Register your models here.
admin.site.register(Patient)
admin.site.register(Pills)
admin.site.register(Days)
admin.site.register(Appointments)