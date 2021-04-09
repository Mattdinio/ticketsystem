from django.shortcuts import render
from django.views import generic
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
    except Ticket.DoesNotExist:
        raise Http404('ticket not found')
    return render (request, 'ticket_detail.html', {
        'ticket' : ticket,
    })

class ticketView(generic.ListView):
    template_name = '/dashboard.html'

    def get_queryset(self):
        return Ticket.objects.all()

#class ticketDetail(generic.DetailView):
    #model = Ticket
    #template_name = '/dashboard/1/.html'
