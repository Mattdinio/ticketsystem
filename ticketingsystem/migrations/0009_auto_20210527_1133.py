# Generated by Django 3.0.3 on 2021-05-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingsystem', '0008_auto_20210527_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='itemImage',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Item Picture'),
        ),
    ]
