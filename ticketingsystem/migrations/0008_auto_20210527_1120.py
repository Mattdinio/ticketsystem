# Generated by Django 3.0.3 on 2021-05-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingsystem', '0007_auto_20210504_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='itemImage',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Item Picture'),
        ),
    ]
