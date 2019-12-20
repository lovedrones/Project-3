from django.db import models

# Create your models here.
class Patient:
  def __init__(self, name, d_o_b, user_relation, healthcare, appointments, pills):
    self.name = name
    self.d_o_b = d_o_b
    self.user_relation = user_relation
    self.healthcare = healthcare
    self.appointments = appointments
    self.pills = pills
    
patients = [
    Patient('Zach', 8132001, 'Back-Man', 'Arkids', [{'name': 'Witch Doctor', 'date': '2019-12-19 17:17:24.943901', 'practioner': 'Nazeebo', 'location': 'Congress Ave, Austin, TX 78704', 'note' : ''}] ,[{'name': 'Joy', 'total': 14, 'days': {'monday': ['0800','0800'], 'tuesday':[''],'wednesday': ['0800'],'thursday': [''],'friday': [''],'saturday': [''],'sunday': ['']}, 'dosage': 3}] ),
    Patient('Marco', 1122000, 'Midle-Man', 'MarcoCare', [], []),
    Patient('Juan', 1011970, 'Front-Man', 'MarcoCare', [] , [])
]

class Pills:
    def __init__(self, name, total, days, times, dosage):
        self.name = name
        self.total = total
        self.days = days
        self.dosage = dosage

class Appointment:
    def __init__(self, name, date, practioner, location, note):
        self.name = name
        self.date = date
        self.practioner = practioner
        self.location = location
        self.note = note