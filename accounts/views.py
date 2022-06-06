from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Nurse, Doctor, Patient, Appointment
import re
from django.contrib import messages
from pages.models import Device

#sign up code for doctor 
def signd(request):
    if request.method == 'POST':
        #variabels
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Photo = request.FILES['photo']
        Address = request.POST['address']
        Ssn = request.POST['ssn']
        Age= request.POST['age']
        Mobil = request.POST['mobil']
        Email = request.POST['email']
        Password = request.POST['pass']
        Confirm_Password = request.POST['conpass']
        doctorup = Doctor(Fname=Fname, Lname=Lname, Photo=Photo, Mobil=Mobil, Email=Email, Password=Password, Confirm_Password=Confirm_Password, Address=Address, SSN=Ssn, Age=Age)
        if Password != Confirm_Password or Doctor.objects.filter(Email = request.POST['email']).exists():
           messages.error(request, "Unsuccessful registration. Invalid information.. retray again!")
           return redirect('signd')
        else:  
           doctorup.save()
           messages.success(request, "Successfully Registered... And We will check" )
           return redirect('signd')
    else:
        return render(request , 'accounts/signd.html')

#sign in code for doctor        
def home2 (request):
    if request.method == "POST":
        if Doctor.objects.filter(Email = request.POST['Email'],Password = request.POST['Password'],status=1).exists():
            data =Doctor.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Doctor.objects.filter(Email = request.POST['Email'])
            appointment = Appointment.objects.all()
            return render(request, 'accounts/doctor.html', {'data': data,'appointment':appointment})
            
        else:
            context={'msg': 'Try again invalid Email or password or not verified Registaration'}
            return render(request , 'accounts/signn.html',context)
#sign up code for Nurse 
def signn(request):
    if request.method == 'POST':
        #variabels
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Photo = request.FILES['photo']
        Address = request.POST['address']
        Ssn = request.POST['ssn']
        Age= request.POST['age']
        Mobil = request.POST['mobil']
        Email = request.POST['email']
        Password = request.POST['pass']
        Confirm_Password = request.POST['conpass']
        nurseup = Nurse(Fname=Fname, Lname=Lname, Photo=Photo, Mobil=Mobil, Email=Email, Password=Password, Confirm_Password=Confirm_Password, Address=Address, SSN=Ssn, Age=Age)
        if Password != Confirm_Password or Nurse.objects.filter(Email = request.POST['email']).exists():
           messages.error(request, "Unsuccessful registration. Invalid information.. retray again!")
           return redirect('signn')
        else:  
           nurseup.save()
           messages.success(request, "Successfully Registered... And We will check" )
           return redirect('signn')
    else:
        return render(request , 'accounts/signn.html') 
#sign in code for Nurse 
def home1(request):
    if request.method == "POST":
        if Nurse.objects.filter(Email = request.POST['Email'],Password = request.POST['Password'], status=1).exists():
            data =Nurse.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Nurse.objects.filter(Email = request.POST['Email'])
            return render(request, 'accounts/nurse.html', {'data': data})
        else:
            context={'msg': 'Try again invalid Email or password or not verified Registaration'}
            return render(request , 'accounts/signn.html',context)

#sign up code for Patient
def signp(request):
    if request.method == 'POST':
        #variabels
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Photo = request.FILES['photo']
        Age= request.POST['age']
        Email = request.POST['email']
        Password = request.POST['pass']
        Confirm_Password = request.POST['conpass']
        patientup = Patient(Fname=Fname, Lname=Lname, Photo=Photo, Email=Email, Password=Password, Confirm_Password=Confirm_Password, Age=Age)
        if Password != Confirm_Password or Patient.objects.filter(Email = request.POST['email']).exists():
           messages.error(request, "Unsuccessful registration. Invalid information.. retray again!")
           return redirect('signp')
        else:  
           patientup.save()
           messages.success(request, "Successfully Registered... And We will check" )
           return redirect('signp')
    else:
        return render(request , 'accounts/signp.html') 

#sign in code for Patient
def home(request):
    if request.method == "POST":
        if Patient.objects.filter(Email = request.POST['Email'],Password = request.POST['Password']).exists():
            data =Patient.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Patient.objects.filter(Email = request.POST['Email'])
            devices = Device.objects.all()
            doctors = Doctor.objects.filter(status=1)
            nurses = Nurse.objects.filter(status=1)
            return render(request, 'accounts/patient.html', {'data': data , 'devices' : devices, 'doctors' : doctors, 'nurses' : nurses })
        else:
            context={'msg': 'Try again invalid Email or password'}
            return render(request , 'accounts/signp.html',context)

# view doctor 
def doctor(request):
    data = Doctor.objects.all()
    x={'data':data}
    return render(request , 'accounts/doctor.html',x)
# view nurse
def nurse(request):
    data = Nurse.objects.all()
    x={'data':data}
    return render(request , 'accounts/nurse.html',x)
# view patient
def patient(request):
    data = Patient.objects.all()
    x={'data':data}
    return render(request , 'accounts/patient.html',x)

def appointmentp(request): 
    if request.method == "POST":
        appointment = Appointment()
        name = request.POST['name']
        Mobil = request.POST['Mobil']
        Email = request.POST['Email']
        date = request.POST['date']
        upload = request.FILES['upload']
        time= request.POST['time']
        appointment.name=name
        appointment.Mobil=Mobil
        appointment.Email= Email
        appointment.date=date
        appointment.upload=upload
        appointment.time= time
        appointment.save()

    return render(request , 'accounts/patient.html')