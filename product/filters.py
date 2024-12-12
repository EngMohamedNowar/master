import django_filters

from .models import Product

class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name ="name", lookup_expr="icontains")

    class Meta:
        model = Product
        # fields = ['category', 'brand']
        fields = ['category', 'brand','keyword']