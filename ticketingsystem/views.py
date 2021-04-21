from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404
from .models import Ticket,Customer
from .forms import *
from .filters import ticketFilter
def home (request):
    return render(request, 'home.html')

def dashboard (request):
    tickets = Ticket.objects.all()
    ticketFilters = ticketFilter()
    context = {'ticketFilters': ticketFilter}
    return render (request, 'dashboard.html', {
       'tickets' : tickets,
    })

def customerList (request):
    customers = Customer.objects.all()
    return render (request, 'customer_list.html', {
       'customers' : customers,
    })


def dashboardList(ListView):
    model = Ticket

def ticket_detail (request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        raise Http404('ticket not found')
    form = ticketForm(instance=ticket)
    if request.method == 'POST':
        form = ticketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
    context = {'form': form.as_p,
    'ticket': ticket}
    return render(request, 'ticket_detail.html', context)
    #return render (request, 'ticket_detail.html', {
    #    'ticket' : ticket,
    #})

class ticketView(generic.ListView):
    template_name = '/dashboard.html'

    def get_queryset(self):
        return Ticket.objects.all()


def createTicket(request):
    form = ticketForm()
    if request.method == 'POST':
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form.as_p}
    return render(request, 'create-ticket.html', context)
