from django.forms import ModelForm
from .models import Customer, Device, Ticket

class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ticketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'