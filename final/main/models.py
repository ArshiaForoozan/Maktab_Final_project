from django.db import models
from django.db.models.enums import Choices

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status_modes = [
        ('InStock', 'InStock'),
        ('OutOfStock', 'OutOfStock'),
    ]
    status = models.CharField(
        max_length=11,
        choices = status_modes,
        default = 'OutOfStock',
    )
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




