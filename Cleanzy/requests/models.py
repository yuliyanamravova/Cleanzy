from django.db import models

from Cleanzy.accounts.models import Account
from Cleanzy.products.models import Product

# Create your models here.
CHOICES = [
    ('5 Litre', '5 Litre'),
    ('10 Litre', '10 Litre'),
    ('15 Litre', '15 Litre'),
    ('25 Litre', '25 Litre'),
]


class Request(models.Model):
    products = models.ManyToManyField(to=Product, related_name='products',)
    package_type = models.CharField(choices=CHOICES, default='5 Litre', max_length=20)
    quantity = models.IntegerField()
    date = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(to=Account, on_delete=models.CASCADE)
