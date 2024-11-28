# Generated by Django 4.2.16 on 2024-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=20)),
                ('phone_number', models.CharField(verbose_name=10)),
                ('address', models.CharField(verbose_name=40)),
                ('products', models.ManyToManyField(blank=True, to='products.product')),
            ],
        ),
    ]
