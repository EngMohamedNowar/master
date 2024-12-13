from django.shortcuts import get_object_or_404, render
from product.filters import ProductsFilter
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view

from.models import Product
from.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    # products =Product.objects.all()
    filter = ProductsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    count = filter.qs.count()
    restPage = 2
    paginator =PageNumberPagination()
    paginator.page_size = restPage
    queryset = paginator.paginate_queryset(filter.qs,request)
    # serializer = ProductSerializer(products, many=True)
    serializer = ProductSerializer(queryset, many=True)
    return Response({'products':serializer.data,'per pages':restPage,'products count':count})
@api_view(['GET'])
def get_by_id_products(request, pk):
    product = get_object_or_404(Product, id =pk)
    serializer = ProductSerializer(product ,many= False)
    return Response({"product":serializer.data})


