# Generated by Django 4.2.16 on 2024-11-04 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_ingredients',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='instructions_for_use',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]