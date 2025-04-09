from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CustomerListViewHTTPClient.as_view(), name='customer_list'),
    path('create/', views.CustomerCreateView2.as_view(), name='customer_create'),
    path('<str:customer_id>/', views.CustomerDetailView2.as_view(), name='customer_details'),
    path('<str:customer_id>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),
]
