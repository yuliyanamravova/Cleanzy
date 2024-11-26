from django.contrib.auth import get_user_model
from django.db import models

from Cleanzy.products.models import Product


user = get_user_model()  # Reference it dynamically

# Create your models here.
CHOICES = [
    ('5 Litre', '5 Litre'),
    ('10 Litre', '10 Litre'),
    ('15 Litre', '15 Litre'),
    ('25 Litre', '25 Litre'),
]


class Request(models.Model):
    products = models.ForeignKey(to=Product, related_name='product', on_delete=models.CASCADE)
    package_type = models.CharField(choices=CHOICES, default='5 Litre', max_length=20)
    quantity = models.IntegerField()
    date = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(to=user, on_delete=models.CASCADE)
