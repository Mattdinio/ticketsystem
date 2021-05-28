from django.forms import ModelForm
from .models import Customer, Ticket, inventoryItem

class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ticketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class inventoryForm(ModelForm):
    class Meta:
        model = inventoryItem
        fields = '__all__'

