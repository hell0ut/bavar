from django.urls import path
from .views import HomePage,item_list


app_name='home'

urlpatterns=[
    path('', item_list, name='home_page',
         )

]