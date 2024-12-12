from django.shortcuts import render
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view

from.models import Product
from.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    products =Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(products)
    return Response({'products':serializer.data})


