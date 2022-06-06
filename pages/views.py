from unicodedata import name
from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse
from accounts.models import Doctor, Nurse
from .models import Device
from multiprocessing import context
from pages.models import ContactUS
#from django.core.mail import send_mail
# Create your views here.

def index(request):
    context={
        'doctors': Doctor.objects.all()
        #'nurses': Nurse.objects.all(),
        #'devices': Device.objects.all()
    }
    return render(request , 'pages/index.html' , context)

def index1(request): 
    if request.method == "POST":
        contact=ContactUS()
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact.email=email
        contact.subject=subject
        contact.message= message
        contact.save()    
    return render(request , 'pages/index.html')
