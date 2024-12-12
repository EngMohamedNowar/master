from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_all_products, name='all_products'),
    path('products/<str:pk>/', views.get_by_id_products, name='products_by_id'),
]

