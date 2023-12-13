from import_export import resources
from .models import District

class DistrictResources(resources.ModelResource):
    class Meta:
        model= District
        fields = ['district_code', 'name', 'region__name']