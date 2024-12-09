# Generated by Django 4.2.16 on 2024-12-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Kitchen', 'Kitchen'), ('Bathroom', 'Bathroom'), ('Floor', 'Floor'), ('Laundry', 'Laundry'), ('Industry', 'Industry')], default='Kitchen'),
        ),
    ]