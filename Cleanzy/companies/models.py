from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(30)
    address = models.CharField(50)
    vat_uic_number = models.CharField(max_length=9, unique=True)
    phone_number = models.CharField(max_length=10)