from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Customer(models.Model):
    firstName = models.CharField (max_length=50, verbose_name="First Name")
    lastName = models.CharField (max_length=50, verbose_name="Last Name")
    # phone number validation
    phoneMessage = 'Phone number must be 11 digits format \'00000000000\''
    phone_regex = RegexValidator(regex='^\\d{11}$',message=phoneMessage)
    number = models.CharField(max_length=11, validators=[phone_regex], verbose_name="Phone Number")
    email = models.EmailField(max_length = 254, blank= True, null=True, verbose_name="Email Address")
    address = models.TextField(blank=True, verbose_name="Address")

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Ticket(models.Model):
    TICKET_STATUS = [('Open', 'Open'), ('Waiting on Customer', 'Waiting on Customer'), ('Waiting for Parts', 'Waiting for Parts'), ('Closed', 'Closed')]
    DEVICE_TYPES = [('Mobile Phone', 'Mobile Phone'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Games Console', 'Games Console'), ('Tablet', 'Tablet'), ('Smart device', 'Smart Device'), ('Other', 'Other')]
    ticketName = models.CharField(max_length=100, verbose_name="Ticket Name")
    deviceMake = models.CharField (max_length=30, verbose_name="Device Make")
    deviceModel = models.CharField(max_length=50, verbose_name="Device Model")
    deviceType = models.CharField(max_length=15, choices=DEVICE_TYPES, verbose_name="Device Type")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Customer")
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=True, related_name="assignedTechnician", verbose_name="Assigned")
    ticketStatus = models.CharField(max_length=30, choices=TICKET_STATUS, verbose_name="Ticket Status")
    createdDate = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Created On")
    createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, editable=False, related_name="createdByTechnician", verbose_name="createdBy")
    lastUpdated = models.DateTimeField(auto_now=True, verbose_name="Last Update Date")
    updatedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, editable=False, related_name="updatedByTechnician", verbose_name="Updated By")
    ticketDescription = models.TextField(verbose_name="Ticket Description")

    def __str__(self):
        return self.ticketName  

    def getAssigned(self):
        return self.assigned
    class meta:
        ordering = ['-id']
        
class inventoryItem(models.Model):
    ITEM_TYPES = [('Mobile Phone', 'Mobile Phone'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Games Console', 'Games Console'), 
    ('Tablet', 'Tablet'), ('Smart device', 'Smart Device'),('Monitor', 'Monitor'), ('Peripherals', 'Peripherals'), ('Component', 'Component'),('Accessory', 'Accessory'), ('Software', 'Software'), ('Other', 'Other')]
    itemName = models.CharField(max_length=150, verbose_name="Item Name")
    itemType = models.CharField(max_length = 50,choices=ITEM_TYPES,verbose_name="Item Type")
    quantityInStock = models.IntegerField (verbose_name="In Stock")
    price = models.DecimalField (decimal_places=2, max_digits=9, verbose_name="Price")
    orderLink = models.URLField(blank = True, verbose_name="Order Link")
    lastOrdered = models.DateTimeField(auto_now=True, verbose_name="Last Ordered On")

    def __str__(self):
        return self.itemName + "(" + self.itemType + ")" 