from django.contrib import admin
from .models import Brand, Region, Category, Country_origin, Manufacturer, Sensortype
# Register your models here.
admin.site.register(Region)
admin.site.register(Category)
@admin.register(Brand)
@admin.register(Country_origin)
@admin.register(Sensortype)
@admin.register(Manufacturer)
class EntityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)