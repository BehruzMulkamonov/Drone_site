from django.urls import path
from .views import BrandApi
urlpatterns = [
    path('brand/', BrandApi.as_view() ),
    path('brand/<int:pk>/', BrandApi.as_view() ),
]
