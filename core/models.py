from django.conf import settings
from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

