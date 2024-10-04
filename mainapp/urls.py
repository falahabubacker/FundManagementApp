from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('add/', views.add, name='add'),
]