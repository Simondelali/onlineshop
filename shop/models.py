from django.db import models
from django.utils.text import slugify

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=False, blank=True)

    def save(self, *args, **kwargs):
        # self.slug = self.name.replace(' ', '-').lower()
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class OrderItem(models.Model):
    ...
class Order(models.Model):
    ...