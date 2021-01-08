from django.contrib import admin
from .models import *
from django import forms

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(SubCategory)


class ImageInline(admin.TabularInline):
    model = Image


class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)
admin.site.register(Item, ItemAdmin)





