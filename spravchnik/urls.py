from django.urls import path

from spravchnik.views.clas.brand import DeleteBrand, ListBrand, CreateBrand, UpdateBrand, DetailBrand
from spravchnik.views.clas.region import ListRegion, DetailRegion, CreateRegion, DeleteRegion, UpdateRegion
from spravchnik.views.clas.category import ListCategory, DetailCategory, CreateCategory, DeleteCategory, UpdateCategory
from spravchnik.views.clas.country_origin import ListOrigin, DeleteOrigin, CreateOrigin, DetailOrigin, UpdateOrigin
from spravchnik.views.clas.manufacturers import ListManufacturer, DeleteManufacturer, CreateManufacturer, DetailManufacturer, UpdateManufacturer
from spravchnik.views.clas.position import ListPosition, DeletePosition, CreatePosition, DetailPosition, UpdatePosition
from spravchnik.views.clas.distric import ListDistrict, DeleteDistrict, CreateDistrict, DetailDistrict, UpdateDistrict, export_district
from spravchnik.views.clas.sensortype import ListType, DeleteType, CreateType, DetailType, UpdateType
# from spravchnik.views import index, delete_brand, create_brand, update_brand

urlpatterns = [
    path('brand/', ListBrand.as_view(), name='brand'),
    path('brand/create/', CreateBrand.as_view(), name='create_brand'),
    path('brand/<int:pk>/update/', UpdateBrand.as_view(), name='update_brand'),
    path('brand/<int:pk>/deleta/', DeleteBrand.as_view(), name='delete_brand'),
    path('brand/<int:pk>/', DetailBrand.as_view(), name='detail_brand'),

    # Region url
    path('region/', ListRegion.as_view(), name='region'),
    path('region/create/', CreateRegion.as_view(), name='create_region'),
    path('region/<int:pk>/update/', UpdateRegion.as_view(), name='update_region'),
    path('region/<int:pk>/deleta/', DeleteRegion.as_view(), name='delete_region'),
    path('region/<int:pk>/', DetailRegion.as_view(), name='detail_region'),

    # Category url
    path('category/', ListCategory.as_view(), name='category'),
    path('category/create/', CreateCategory.as_view(), name='create_category'),
    path('category/<int:pk>/update/', UpdateCategory.as_view(), name='update_category'),
    path('category/<int:pk>/deleta/', DeleteCategory.as_view(), name='delete_category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='detail_category'),

    # Country_origin
    path('origin/', ListOrigin.as_view(), name='origin'),
    path('origin/create/', CreateOrigin.as_view(), name='create_origin'),
    path('origin/<int:pk>/update/', UpdateOrigin.as_view(), name='update_origin'),
    path('origin/<int:pk>/deleta/', DeleteOrigin.as_view(), name='delete_origin'),
    path('origin/<int:pk>/', DetailOrigin.as_view(), name='detail_origin'),

    # Manufacturer urls
    path('manufacturer/', ListManufacturer.as_view(), name='manufacturer'),
    path('manufacturer/create/', CreateManufacturer.as_view(), name='create_manufacturer'),
    path('manufacturer/<int:pk>/update/', UpdateManufacturer.as_view(), name='update_manufacturer'),
    path('manufacturer/<int:pk>/deleta/', DeleteManufacturer.as_view(), name='delete_manufacturer'),
    path('manufacturer/<int:pk>/', DetailManufacturer.as_view(), name='detail_manufacturer'),

    # Position
    path('position/', ListPosition.as_view(), name='position'),
    path('position/create/', CreatePosition.as_view(), name='create_position'),
    path('position/<int:pk>/update/', UpdatePosition.as_view(), name='update_position'),
    path('position/<int:pk>/deleta/', DeletePosition.as_view(), name='delete_position'),
    path('position/<int:pk>/', DetailPosition.as_view(), name='detail_position'),

    # district 
    path('district/', ListDistrict.as_view(), name='district'),
    path('district/create/', CreateDistrict.as_view(), name='create_district'),
    path('district/<int:pk>/update/', UpdateDistrict.as_view(), name='update_district'),
    path('district/<int:pk>/deleta/', DeleteDistrict.as_view(), name='delete_district'),
    path('district/<int:pk>/', DetailDistrict.as_view(), name='detail_district'),
    path('export-csv', export_district, name='export_csv'),


    # sensortype
    path('sensortype/', ListType.as_view(), name='sensortype'),
    path('sensortype/create/', CreateType.as_view(), name='create_sensortype'),
    path('sensortype/<int:pk>/update/', UpdateType.as_view(), name='update_sensortype'),
    path('sensortype/<int:pk>/deleta/', DeleteType.as_view(), name='delete_sensortype'),
    path('sensortype/<int:pk>/', DetailType.as_view(), name='detail_sensortype'),


]


