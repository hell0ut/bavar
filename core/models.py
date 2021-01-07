from django.conf import settings
from django.db import models
from djrichtextfield.models import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name='Категория')

    def items(self):
        return Item.objects.filter(category__parentCategory=self)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name='Подкатегория')
    parentCategory = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subs')

    def __str__(self):
        return self.parentCategory.title + ' | ' + self.title


class Item(models.Model):
    title = models.CharField(max_length=100,verbose_name='Товар')
    price = models.FloatField(verbose_name='Цена',default=0)
    quanity = models.IntegerField(verbose_name='Количество',default=1000)
    description = RichTextField(verbose_name='Описание',null=True)
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=None,null=True,related_name='items')

    def main_photo(self):
        return self.images.first()

    def __str__(self):
        return self.title


class Image(models.Model):
    #name = models.CharField(max_length=255,null=True,default='def')
    image = models.ImageField(upload_to='images/')
    #default = models.BooleanField(default=False)
    #width = models.FloatField(default=100)
    #length = models.FloatField(default=100)
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE,null=True)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    order_quanity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def items(self):
        return self.items.all()

    def total(self):
        return sum([item.price*item.order_quanity for item in self.get_cart_items()])

    def __str__(self):
        return f'{self.user}'

