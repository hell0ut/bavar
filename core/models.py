from django.conf import settings
from django.db import models
from djrichtextfield.models import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')

    def items(self):
        return Item.objects.filter(category__parent_category=self)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Подкатегория')
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subs')

    def __str__(self):
        return self.parent_category.title + ' | ' + self.title


class Item(models.Model):
    title = models.CharField(max_length=100,verbose_name='Товар')
    price = models.FloatField(verbose_name='Цена', default=0)
    quantity = models.IntegerField(verbose_name='Количество товара на складе', default=0)
    description = RichTextField(verbose_name='Описание', null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=None, null=True, related_name='items')

    def main_photo(self):
        return self.images.first()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'Картинка для товара {self.item}'


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_items(self):
        return self.items.all()

    def total(self):
        return sum([cart_item.item.price * cart_item.quantity for cart_item in self.get_items()])


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.item.title} в количестве: {self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Заказчик')

    shipping_address = models.TextField(verbose_name='Адрес получателя')
    ordered_date = models.DateTimeField(auto_now=True, verbose_name='Время заказа')
    # спосіб оплати можна додати після уточнення, які саме способи доступні в магазині

    UNCONFIRMED = 1
    CONFIRMED = 2
    ASSEMBLED = 3
    SHIPPED = 4
    ACCEPTED_BY_USER = 5
    CANCELED = 6

    ORDER_STATUS_CHOICES = [
        (UNCONFIRMED, 'Ожидает подтверждения'),
        (CONFIRMED, 'Подтвержденный администратором'),
        (ASSEMBLED, 'Комплектуется'),
        (SHIPPED, 'Передан в службу доставки'),
        (ACCEPTED_BY_USER, 'Получен заказчиком'),
        (CANCELED, 'Отменен')
    ]

    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=UNCONFIRMED, verbose_name='Статус')

    def get_items(self):
        return self.items.all()

    def total(self):  # consider returning integer
        return sum([order_item.item.price * order_item.quantity for order_item in self.get_items()])

    def __str__(self):
        return f'Заказ пользователя {self.user.first_name} {self.user.last_name}'

    def order(self):
        return self.__str__()


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return f'Товар {self.item.title} в количестве {self.quantity}'

    def price_for_1_item(self):  # consider returning integer
        return self.item.price

    def subtotal(self):  # consider returning integer
        return self.item.price * self.quantity
