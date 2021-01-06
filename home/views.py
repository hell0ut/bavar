from django.shortcuts import render
from django.views.generic import TemplateView


from ..core.models import Item
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home/home.html'


