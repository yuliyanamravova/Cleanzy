from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def pattern_validator(value:str):
    if value[0].isalpha() and value[1].isalpha():
        for char in value:
            if not char.isdigit():
                raise ValidationError('The VAT/UIC number is not valid.')
    else:
        raise ValidationError('The VAT/UIC number must start with 2 letters representing the country code.')


class Company(models.Model):
    name = models.CharField(30)
    address = models.CharField(50)
    vat_uic_number = models.CharField(max_length=10, unique=True, validators=[pattern_validator])
    phone_number = models.CharField(13, validators=[MinLengthValidator(10)])
