from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', views.home),
    path('home1/', views.home1),
    path('home2/', views.home2),
]