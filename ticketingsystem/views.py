from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Ticket,Customer,Device

def home (request):
    return render(request, 'home.html')

def dashboard (request):
    tickets = Ticket.objects.all()
    return render (request, 'dashboard.html', {
       'tickets' : tickets,
    })

def ticket_detail (request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except ticket.DoesNotExist:
        raise Http404('ticket not found')
    return render (request, 'ticket_detail.html', {
        'ticket' : ticket,
    })