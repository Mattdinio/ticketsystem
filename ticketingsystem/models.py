from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Device(models.Model):
    DEVICE_TYPES = [('Mobile Phone', 'Mobile Phone'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Games Console', 'Games Console'), ('Tablet', 'Tablet'), ('Smart device', 'Smart Device'), ('Other', 'Other')]
    deviceMake = models.CharField (max_length=30)
    deviceModel = models.CharField(max_length=50)
    deviceType = models.CharField(max_length=15, choices=DEVICE_TYPES)
    deviceDescription = models.TextField(blank=True)

    def __str__(self):
        return self.deviceMake + ' ' + self.deviceModel

    class meta:
        ordering = ['deviceMake']



class CommonPeopleInfo(models.Model):
    firstName = models.CharField (max_length=50)
    lastName = models.CharField (max_length=50)
    # phone number validation
    phoneMessage = 'Phone number must be 11 digits format \'00000000000\''
    phone_regex = RegexValidator(regex='^\\d{11}$',message=phoneMessage)
    number = models.CharField(max_length=11, validators=[phone_regex])
    email = models.EmailField(max_length = 254, null=True)

    class Meta:
        abstract = True

class Customer(CommonPeopleInfo):
    address = models.TextField(blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Ticket(models.Model):
    TICKET_STATUS = [('Open', 'Open'), ('Waiting on Customer', 'Waiting on Customer'), ('Waiting for Parts', 'Waiting for Parts'), ('Closed', 'Closed')]
    ticketName = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    createdDate = models.DateTimeField(auto_now_add=True, editable=False)
    lastUpdated = models.DateTimeField(auto_now=True)
    ticketDescription = models.TextField()
    ticketStatus = models.CharField(max_length=30, choices=TICKET_STATUS)

    def __str__(self):
        return self.ticketName

    class meta:
        ordering = ['-id']
