from django.db import models

from Cleanzy.products.models import Product


# Create your models here.


class Warehouse(models.Model):
    town = models.CharField(max_length=20)
    phone_number = models.CharField(10)
    address = models.CharField(40)
    products = models.ManyToManyField(to=Product, blank=True)
