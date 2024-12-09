# Generated by Django 4.2.16 on 2024-12-09 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10)], verbose_name=13),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='town',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
