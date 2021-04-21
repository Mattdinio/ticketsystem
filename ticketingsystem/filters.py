import django_filters

from .models import *

class ticketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = '__all__'