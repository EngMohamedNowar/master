from django.db import models

# Create your models here.
class Category(models.Model):
    plants = "plants" 
    seeds = "seeds"
    pots = "pots"
    
class Product(models.Model):
    name = models.CharField(max_length=255,default='',blank=False)
    description = models.TextField(max_length=1000,default='', blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    brand = models.CharField(max_length=200, default='', blank=False)
    category = models.CharField(max_length=200,choices= Category)

