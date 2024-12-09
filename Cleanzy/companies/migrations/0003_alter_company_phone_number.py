# Generated by Django 4.2.16 on 2024-12-09 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_vat_uic_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10)], verbose_name=13),
        ),
    ]
