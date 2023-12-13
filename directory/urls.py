from django.urls import path
from directory.view.clas.organization import ListOrg, DeleteOrg, CreateOrg, DetailOrg, UpdateOrg
from directory.view.clas.drone import ListDrone, DeleteDrone, CreateDrone, DetailDrone, UpdateDrone
from directory.view.clas.employee import ListEmp, DeleteEmp, CreateEmp, DetailEmp, UpdateEmp
from directory.view.clas.sensor import ListSensor, DeleteSensor, CreateSensor, DetailSensor, UpdateSensor
from directory.view.clas.object import ListObject, DeleteObject, CreateObject, DetailObject, UpdateObject
# from spravchnik.views import index, delete_brand, create_brand, update_brand

urlpatterns = [
    path('organization/', ListOrg.as_view(), name='organization'),
    path('organization/create/', CreateOrg.as_view(), name='create_organization'),
    path('organization/<int:pk>/update/', UpdateOrg.as_view(), name='update_organization'),
    path('organization/<int:pk>/deleta/', DeleteOrg.as_view(), name='delete_organization'),
    path('organization/<int:pk>/', DetailOrg.as_view(), name='detail_organization'),


    # drone urls
    path('drone/', ListDrone.as_view(), name='drone'),
    path('drone/create/', CreateDrone.as_view(), name='create_drone'),
    path('drone/<int:pk>/update/', UpdateDrone.as_view(), name='update_drone'),
    path('drone/<int:pk>/deleta/', DeleteDrone.as_view(), name='delete_drone'),
    path('drone/<int:pk>/', DetailDrone.as_view(), name='detail_drone'),


    # emp urls 
    path('employee/', ListEmp.as_view(), name='employee'),
    path('employee/create/', CreateEmp.as_view(), name='create_employee'),
    path('employee/<int:pk>/update/', UpdateEmp.as_view(), name='update_employee'),
    path('employee/<int:pk>/deleta/', DeleteEmp.as_view(), name='delete_employee'),
    path('employee/<int:pk>/', DetailEmp.as_view(), name='detail_employee'),

    # sensor url 
    path('sensor/', ListSensor.as_view(), name='sensor'),
    path('sensor/create/', CreateSensor.as_view(), name='create_sensor'),
    path('sensor/<int:pk>/update/', UpdateSensor.as_view(), name='update_sensor'),
    path('sensor/<int:pk>/deleta/', DeleteSensor.as_view(), name='delete_sensor'),
    path('sensor/<int:pk>/', DetailSensor.as_view(), name='detail_sensor'),

    # object url 
    path('object/', ListObject.as_view(), name='object'),
    path('object/create/', CreateObject.as_view(), name='create_object'),
    path('object/<int:pk>/update/', UpdateObject.as_view(), name='update_object'),
    path('object/<int:pk>/deleta/', DeleteObject.as_view(), name='delete_object'),
    path('object/<int:pk>/', DetailObject.as_view(), name='detail_object'),
]
