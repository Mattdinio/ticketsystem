from django.contrib import admin
from .models import Ticket,Customer,inventoryItem



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticketName', 'assigned', 'customer', 'createdDate', 'lastUpdated', 'ticketStatus', 'ticketDescription')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'number', 'email', 'address')

@admin.register(inventoryItem)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id','itemName', 'itemType', 'quantityInStock','price','orderLink','lastOrdered')