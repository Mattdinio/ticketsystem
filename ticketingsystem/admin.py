from django.contrib import admin

from .models import Device,Ticket,Customer

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('deviceMake', 'deviceModel', 'deviceType', 'deviceDescription')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticketName', 'createdDate', 'lastUpdated', 'ticketStatus', 'ticketDescription')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'number', 'email', 'address')