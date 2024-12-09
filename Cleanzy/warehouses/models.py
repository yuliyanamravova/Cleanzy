from django.core.validators import MinLengthValidator
from django.db import models

from Cleanzy.products.models import Product


# Create your models here.


class Warehouse(models.Model):
    town = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    phone_number = models.CharField(13, validators=[MinLengthValidator(10)])
    address = models.CharField(40)
    products = models.ManyToManyField(to=Product, blank=True)
