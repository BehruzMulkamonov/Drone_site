from django.shortcuts import render
from .serializers import  BrandSerializer
from spravchnik.models import Brand
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# class BrandApi(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
    
class BrandApi(APIView):


    def get(self, request, pk=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        # pk = kwargs.get('pk', None)
        # if not pk:
        #     return Response({'error':'Not none'})
        try:
            instance = Brand.objects.get(pk=pk)
        except:
            return Response({'message': 'Bu idda malumot yuq'})
        serializer = BrandSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
