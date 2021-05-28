from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Ticket,Customer,inventoryItem
from .forms import *
from .filters import ticketFilter
from django.contrib.auth.models import User
import django_filters

# Homepage
def home (request):
    return render(request, 'home.html')

# Dashboard
def dashboard (request):
    tickets = Ticket.objects.all()
    ticketFilters = ticketFilter()
    context = {'ticketFilters': ticketFilter}
    return render (request, 'dashboard.html', {
       'tickets' : tickets,
    })

def dashboardList(ListView):
    model = Ticket

class ticketView(generic.ListView):
    template_name = '/dashboard.html'

    def get_queryset(self):
        return Ticket.objects.all()

# Ticket Detail
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
            return HttpResponseRedirect('/dashboard/')
    context = {'form': form.as_p,
    'ticket': ticket}
    return render(request, 'ticket_detail.html', context)

# Creating a Ticket
def createTicket(request):
    form = ticketForm()
    if request.method == 'POST':
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    context = {'form':form.as_p}
    return render(request, 'create-ticket.html', context)

# My Tickets
def myTickets (request):
    tickets = Ticket.objects.all()
    ticketFilter = tickets.filter(assigned=request.user)
    return render (request, 'my_tickets.html', {
       'tickets' : tickets,
       'ticketFilter' : ticketFilter
    })

# Customer List
def customerList (request):
    customers = Customer.objects.all()
    return render (request, 'customer_list.html', {
       'customers' : customers,
    })

# Creating a Customer
def createCustomer(request):
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customer_list/')
    context = {'form':form.as_p}
    return render(request, 'create_customer.html', context)

# Stock List
def stockList (request):
    stock = inventoryItem.objects.all()
    return render (request, 'stock_list.html', {
       'stock' : stock,
    })

# create Stock
def createStock(request):
    form = inventoryForm()
    if request.method == 'POST':
        form = inventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stock_list/')
    context = {'form':form.as_p}
    return render(request, 'create_stock.html', context)

def editStock(request, stock_id):
    try:
        stock = inventoryItem.objects.get(id=stock_id)
    except inventoryItem.DoesNotExist:
        raise Http404('stock not found')
    form = inventoryForm(instance=stock)
    if request.method == 'POST':
        form = inventoryForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stock_list/')
    context = {'form': form.as_p,
    'stock': stock}
    return render(request, 'stock_edit.html', context)
