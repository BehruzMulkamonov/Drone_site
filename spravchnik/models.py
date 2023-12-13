from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        verbose_name_plural = "Brands"
        verbose_name = "Brand"

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
class Country_origin(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Country_origins"
        verbose_name = "Country_origin"

class Manufacturer(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "manufacturers"
        verbose_name = "manufacturer"

class Position(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "positions"
        verbose_name = "postion"
    

class Region(models.Model):
    region_code = models.CharField(max_length=30)
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "regions"
        verbose_name = "region"
    
class District(models.Model):
    district_code = models.CharField(max_length=155)
    name = models.CharField(max_length=155)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")


    class Meta:
        verbose_name_plural = "Districts"
        verbose_name = "District"

    def __str__(self):
        return self.name
    

class Sensortype(models.Model):
    name = models.CharField(max_length=155)
    
    class Meta:
        verbose_name_plural = "Sensortypes"
        verbose_name = "Sensortype"

    def __str__(self):
        return self.name
    