from django import forms
from django.forms import ModelForm

from spravchnik.models import Brand, Category, Region, Country_origin, Manufacturer, Position, District, Sensortype

class BrandModelForm(ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)
        labels = {
            'name': 'Brand name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter brand name...'
                }
            ),
        }

# CategoryForm

class CategoryModelForm(ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Category name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Category name...'
                }
            ),
        }

# Region 
class RegionModelForm(ModelForm):
    class Meta:
        model = Region
        fields = ('name', 'region_code')
        labels = {
            'name': 'Region name',
            'region_code': 'Region code'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter region name...'
                }
            ),
            'region_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Region kodni kirit...'
                }
            ),
        }
        
# Country origin
class Country_origin_ModelForm(ModelForm):

    class Meta:
        model = Country_origin
        fields = ('name',)
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

# Manufacturers
class Manufacturer_ModelForm(ModelForm):

    class Meta:
        model = Manufacturer
        fields = ('name',)
        labels = {
            'name': 'Manufacturers name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Manufacturer name...'
                }
            ),
        }


class Position_ModelForm(ModelForm):

    class Meta:
        model = Position
        fields = ('name',)
        labels = {
            'name': 'Position name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter POsition name...'
                }
            ),
        }

class District_ModelForm(ModelForm):

    class Meta:
        model = District
        fields = ( 'district_code', 'name', 'region')
        labels = {
            'name': 'District name',
            'district_code': 'District code',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter District name...'
                }
            ),
            # 'district_code': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Enter District code...'
            #     }
            # )
        }

# sensortype

class SensortypeModelForm(ModelForm):

    class Meta:
        model = Sensortype
        fields = ('name',)
        labels = {
            'name': 'SensorType name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter SensorType name...'
                }
            ),
        }
