from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from ticketingsystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path ('', views.home, name = 'home'),
    path ('dashboard/', views.dashboard, name = 'Dashboard'),
    path ('dashboard/tickets/<int:ticket_id>/', views.ticket_detail, name = 'Ticket_Detail'),
    path ('dashboard/create-ticket/', views.createTicket, name = 'create-ticket'),
    path ('customer_list/', views.customerList, name = 'Customer_List'),
    path ('customer_list/create_customer/', views.createCustomer, name = 'create_customer'),
    path ('my_tickets/', views.myTickets, name = 'my-tickets'),
    path ('stock_list/', views.stockList,  name = 'stock-list'),
    path ('stock_list/create_stock/', views.createStock,  name = 'create_stock'),
    path ('stock_list/<int:stock_id>/', views.editStock, name = 'stock_edit'),
]
