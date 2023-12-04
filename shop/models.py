from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(default='item')

    def __str__(self):
        return self.name
    

class OrderItem(models.Model):
    ...
class Order(models.Model):
    ...