from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product_details
from .serializers import ProductSerializers
 
class Product_details_view (viewsets.ModelViewSet):
   queryset=Product_details.objects.all().order_by('create_ts')
   serializer_class=ProductSerializers
