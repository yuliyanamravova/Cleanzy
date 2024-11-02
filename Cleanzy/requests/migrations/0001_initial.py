# Generated by Django 4.2.16 on 2024-11-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(choices=[('5 Litre', '5 Litre'), ('10 Litre', '10 Litre'), ('15 Litre', '15 Litre'), ('25 Litre', '25 Litre')], default='5 Litre', max_length=20)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('products', models.ManyToManyField(related_name='products', to='products.product')),
            ],
        ),
    ]
