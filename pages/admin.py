from django.contrib import admin
from .models import Device
from .models import Device, ContactUS
# Register your models here.
admin.site.register(Device)
admin.site.register(ContactUS)
