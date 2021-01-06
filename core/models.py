from django.conf import settings
from django.db import models
from djrichtextfield.models import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name='Категория')

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name='Подкатегория')
    parentCategory = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.parentCategory.title + ' | ' + self.title


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


class Item(models.Model):
    title = models.CharField(max_length=100,verbose_name='Товар')
    price = models.FloatField(verbose_name='Цена',default=0)
    quanity = models.IntegerField(verbose_name='Количество',default=1000)
    description = RichTextField(verbose_name='Описание',null=True)
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=None,null=True)
    album=models.ForeignKey(ImageAlbum,related_name='model',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


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

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.price*item.order_quanity for item in self.get_cart_items()])

    def __str__(self):
        return f'{self.user}'

