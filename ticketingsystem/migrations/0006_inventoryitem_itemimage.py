# Generated by Django 3.0.3 on 2021-05-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingsystem', '0005_auto_20210503_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='itemImage',
            field=models.ImageField(blank=True, upload_to='static/images/stock', verbose_name='Item Picture'),
        ),
    ]