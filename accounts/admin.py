from django.contrib import admin
from .models import Doctor
from .models import Nurse
from .models import Patient
from .models import Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Appointment)