from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CustomerListView2.as_view(), name='customer_list'),
    path('create/', views.temp, name='customer_create'),
    path('<str:customer_id>/', views.CustomerDetailView.as_view(), name='customer_details'),
    path('<str:customer_id>/delete', views.temp, name='customer_delete'),
]
