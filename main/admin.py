from django.contrib import admin
from .models import Sensor, Sensordata
# Register your models here.

admin.site.register(Sensor)
admin.site.register(Sensordata)
