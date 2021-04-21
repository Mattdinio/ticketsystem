# Generated by Django 3.0.3 on 2021-04-20 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketingsystem', '0003_auto_20210419_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedTechnician', to=settings.AUTH_USER_MODEL, verbose_name='Assigned'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='createdBy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdByTechnician', to=settings.AUTH_USER_MODEL, verbose_name='createdBy'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketingsystem.Customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='deviceMake',
            field=models.CharField(max_length=30, verbose_name='Device Make'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='deviceModel',
            field=models.CharField(max_length=50, verbose_name='Device Model'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='deviceType',
            field=models.CharField(choices=[('Mobile Phone', 'Mobile Phone'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Games Console', 'Games Console'), ('Tablet', 'Tablet'), ('Smart device', 'Smart Device'), ('Other', 'Other')], max_length=15, verbose_name='Device Type'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lastUpdated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Update Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketDescription',
            field=models.TextField(verbose_name='Ticket Description'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketName',
            field=models.CharField(max_length=100, verbose_name='Ticket Name'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketStatus',
            field=models.CharField(choices=[('Open', 'Open'), ('Waiting on Customer', 'Waiting on Customer'), ('Waiting for Parts', 'Waiting for Parts'), ('Closed', 'Closed')], max_length=30, verbose_name='Ticket Status'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updatedBy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updatedByTechnician', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
    ]