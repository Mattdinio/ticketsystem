# Generated by Django 3.0.3 on 2021-06-01 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingsystem', '0012_auto_20210601_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Price'),
        ),
    ]