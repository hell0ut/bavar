from django.shortcuts import render
from .models import Item
# Create your views here.
def item_list(request):
    context ={
        'items': Item.objects.all()
    }
    return render(request,template_name='home/item_list.html', context=context)

def home(request):
    return render(request,'core/home-page.html')