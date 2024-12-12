from django.shortcuts import get_object_or_404, render
from product.filters import ProductsFilter
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view

from.models import Product
from.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    # products =Product.objects.all()
    filter = ProductsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    # serializer = ProductSerializer(products, many=True)
    serializer = ProductSerializer(filter.qs, many=True)
    return Response({'products':serializer.data})
@api_view(['GET'])
def get_by_id_products(request, pk):
    product = get_object_or_404(Product, id =pk)
    serializer = ProductSerializer(product ,many= False)
    return Response({"product":serializer.data})


