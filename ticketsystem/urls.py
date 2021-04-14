from django.contrib import admin
from django.urls import path

from ticketingsystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name = 'home'),
    path ('dashboard/', views.dashboard, name = 'Dashboard'),
    path ('dashboard/tickets/<int:ticket_id>/', views.ticket_detail, name = 'Ticket_Detail'),
    path ('dashboard/create-ticket/', views.createTicket, name = 'create-ticket'),
]
