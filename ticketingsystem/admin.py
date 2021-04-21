from django.contrib import admin
from .models import Ticket,Customer



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticketName', 'assigned', 'customer', 'createdDate', 'lastUpdated', 'ticketStatus', 'ticketDescription')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'number', 'email', 'address')