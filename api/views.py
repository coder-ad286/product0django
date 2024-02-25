from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from .models import Product
# Create your views here.

@api_view(["GET"])
def apiOverview(req):
    api_urls={
        'List' : '/product-list/',
        'Detail View':'/product-detail/<int:id>',
        'Create' : '/product-create/',
        'Update' : '/product-update/<int:id>',
        'Delete' : '/product-delete/<int:id>'
    }
    
    return Response(api_urls)

@api_view(['GET'])
def fetchProducts(req):
    products = Product.objects.all()
    serializers = ProductSerializers(products,many=True)
    return Response(products)