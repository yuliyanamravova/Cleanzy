from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
def length_validator(code):
    if len(code) != 6 or not code.isdigit():
        raise ValidationError('Product code must be exactly 6 digits!')


CHOICES = [
    ('Kitchen', 'Kitchen'),
    ('Bathroom', 'Bathroom'),
    ('Floor', 'Floor'),
    ('Laundry', 'Laundry'),
    ('Industry', 'Industry')
]


class Product(models.Model):
    name = models.CharField(
        max_length=20
    )
    photo = models.ImageField(upload_to='images/', default='images/default-product.jpg', validators=[])
    code = models.CharField(
        validators=[length_validator]
    )
    description = models.TextField(
        blank=True, null=True,
    )
    ph = models.DecimalField(decimal_places=2, max_digits=4)
    ingredients = models.TextField(
        max_length=300,
        blank=True, null=True,
    )
    price = models.DecimalField(decimal_places=2, max_digits=5)
    instructions = models.TextField()
    group = models.CharField(choices=CHOICES, default='Kitchen')

    def __str__(self):
        return self.name


