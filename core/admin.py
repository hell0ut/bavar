from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    model = Item

    list_display = ('title', 'price', 'quantity')


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0
    # consider making some fields readonly
    readonly_fields = (OrderItem.price_for_1_item, OrderItem.subtotal)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemAdmin]

    list_display = (Order.order, Order.total, 'status')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["user", 'shipping_address', 'ordered_date', Order.total]
        else:
            return []


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Image)





