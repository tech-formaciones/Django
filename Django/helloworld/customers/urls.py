from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.customers_list, name='customers_list'),
    path('create/', views.temp, name='customers_create'),
    path('<str:customer_id>/', views.customer_detail, name='customer_detail'),             # una llamada POST actualiza
    path('<str:customer_id>/delete/', views.temp, name='customer_delete'),
]