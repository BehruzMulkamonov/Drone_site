from django.contrib import admin

# Register your models here.

from django.contrib import admin
from directory.models import Drone, Employee, Organization, Sensor, Object



admin.site.register(Drone)

admin.site.register(Employee)

admin.site.register(Organization)

admin.site.register(Sensor)

admin.site.register(Object)
