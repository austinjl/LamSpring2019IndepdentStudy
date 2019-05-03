from django.urls import path

from . import views

app_name = 'burgerForm'
urlpatterns = [
    path('tickets/', views.tickets, name='tickets'),
    path('tickets/new/', views.order_new, name ='order_new'),
]
