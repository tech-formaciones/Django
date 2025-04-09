from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views
from .views import HomeView


urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('home/', HomeView.as_view(), name='home'),
]