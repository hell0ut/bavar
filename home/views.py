from django.shortcuts import render
from django.views.generic import ListView,DetailView
from core.models import Category,Item

# Create your views here.


class HomePage(ListView):
    template_name = 'home/home.html'
    model = Category

class CategoryDetail(DetailView):
    model = Category
    template_name = 'home/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged']=self.request.user.is_authenticated
        return context

class ItemDetail(DetailView):
    model = Item
    template_name = 'home/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged']=self.request.user.is_authenticated
        return context




