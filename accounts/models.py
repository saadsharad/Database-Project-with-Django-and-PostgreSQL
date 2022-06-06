from distutils.command.upload import upload
from email.headerregistry import Address
from re import M
from django.db import models
from datetime import datetime
from django.utils import timezone

# Doctor Tabel.
class Doctor(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Photo = models.ImageField( upload_to='photos/%Y/%m/%d',blank=True, null=True)
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Confirm_Password = models.CharField(max_length=8, null=True)
    Address = models.CharField(max_length=60)
    SSN = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()

    def __str__(self):
        return self.Fname
  
# Nurse Tabel.
class Nurse(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Photo = models.ImageField( upload_to='photos/%Y/%m/%d', null=True )
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Confirm_Password = models.CharField(max_length=8, null=True)
    Address = models.CharField(max_length=60)
    SSN = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()

    def __str__(self):
        return self.Fname
  # patient Tabel.
class Patient(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Photo = models.ImageField( upload_to='photos/%Y/%m/%d', null=True )
    Age= models.PositiveIntegerField()
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Confirm_Password = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.Fname

class Appointment(models.Model):
    name = models.CharField(max_length=30)
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    date = models.DateField()
    upload = models.FileField( upload_to='uploads/%Y/%m/%d' )

    time= models.TimeField()

    def __str__(self):
        return self.name
