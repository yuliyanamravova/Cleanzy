from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
def length_validator(code):
    if len(code) != 6 and not code.isdigit():
        raise ValidationError('Product code must be exactly 6 digits!')


class Product(models.Model):
    product_name = models.CharField(
        max_length=20
    )
    product_code = models.CharField(
        validators=[length_validator]
    )
    product_description = models.TextField(
        max_length=300,
        blank=True, null=True,
    )
    product_ingredients = models.TextField(
        max_length=300,
        blank=True, null=True,
    )
    price = models.DecimalField(decimal_places=2, max_digits=3)
    instructions_for_use = models.TextField()

    def __str__(self):
        return self.product_name
