from django import forms
from django.forms import ModelForm
from .models import Organization, Drone, Object, Sensor, Employee

class Organization_ModelForm(ModelForm):

    class Meta:
        model = Organization
        fields = ('name', 'category', 'level', 'region', 
                  'district', 'address', 'latitude', 
                  'longitude')
        labels = {
            'name': 'Country_origin name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Country origin name...'
                }
            ),
        }


# Drone form  

class Drone_ModelForm(ModelForm):

    class Meta:
        model = Drone
        fields = ('name', 'brand', 'model', 'manufacturer', 
                  'country_origin', 'production_year', 'mood', 
                  'owner', 'operator', 'status')
        labels = {
            'name': 'Drone name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Drone name...'
                }
            ),
        }      


class Emp_ModelForm(ModelForm):

    class Meta:
        model = Employee
        fields = ('brand', 'first_name', 'last_name', 'surname', 
                  'organization', 'position', 'birthday', 
                  'place_of_birth', 'pasport_data')
        labels = {
            'name': 'Employee name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Employee name...'
                }
            ),
        }      

class Sensor_ModelForm(ModelForm):

    class Meta:
        model = Sensor
        fields = ('sensor_id', 'name', 'type', 'model', 
                  'manufacturer', 'country_origin', 'production_year', 
                  'condition', 'status', 'type_host', 'host_id')
        labels = {
            'name': 'Sensor name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Sensor name...'
                }
            ),
        }      


    # Objects from 

class Object_ModelForm(ModelForm):

    class Meta:
        model = Object
        fields = ('name', 'category', 'level', 'region', 
                  'district', 'address', 'latitude', 
                  'longitude')
        labels = {
            'name': 'Object name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Object name...'
                }
            ),
        }      