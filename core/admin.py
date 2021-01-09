from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image


class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class OrderAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["user", 'cart', 'shipping_address', 'ordered_date']
        else:
            return []


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Image)





