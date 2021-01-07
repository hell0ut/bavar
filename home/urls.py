from django.urls import path
from .views import *


app_name='home'

urlpatterns=[
    path('', HomePage.as_view(), name='home_page'),
    path('<int:pk>/', CategoryDetail.as_view(), name = 'category_detail'),
    path('<int:category_pk>/<int:pk>/',ItemDetail.as_view(),name = 'item_detail')


]