from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(5)]
    )
    first_name = models.CharField(
        max_length=40,
    )
    last_name = models.CharField(
        max_length=40,
    )
    email = models.EmailField()
    password = models.CharField()

