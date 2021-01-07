from django.shortcuts import render
from django.views.generic import ListView
from core.models import Category,SubCategory

# Create your views here.


class HomePage(ListView):
    template_name = 'home/home.html'
    model = Category



