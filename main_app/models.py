from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Days(models.Model):
  name = models.CharField(max_length=10, default='', blank=True)
  monday = ArrayField(
      ArrayField(
        models.CharField(default='' , max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  tuesday = ArrayField(
      ArrayField(
        models.CharField(default='' , max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  wednesday = ArrayField(
      ArrayField(
         models.CharField(default='', max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  thursday = ArrayField(
      ArrayField(
        models.CharField(default='', max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  friday = ArrayField(
      ArrayField(
        models.CharField(default='', max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  saturday = ArrayField(
      ArrayField(
        models.CharField(default='', max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  sunday = ArrayField(
      ArrayField(
        models.CharField(default='', max_length=5, blank=True),
        size=4
  ),
    size=4, blank=True
  )
  
  def __arry__(self):
    return self.name


class Pills(models.Model):
  name = models.CharField(max_length=80)
  total = models.IntegerField()
  pil_days = models.ManyToManyField(Days)
  dosage = models.IntegerField()
  def __str__(self):
    return self.name

class Appointments(models.Model):
  name = models.CharField(max_length=60)
  app_date = models.DateField()
  practioner = models.CharField(max_length=60)
  location = models.CharField(max_length=100)
  note = models.TextField()
  def __str__(self):
    return self.name

class Patient(models.Model):
  name = models.CharField(max_length=60)
  d_o_b = models.DateField()
  user_relation = models.CharField(max_length=30)
  healthcare = models.CharField(max_length=50)
  pills = models.ManyToManyField(Pills)
  appointments = models.ManyToManyField(Appointments)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  
