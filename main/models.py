from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey, OneToOneField
from user_features.models import CustomUser
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null = True, blank = True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null = True)
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

    # @property
    # def thumbnail_preview(self):
    #     if self.image:
    #         return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
    #     return ""


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OnlineShop(models.Model):
    product = models.ManyToManyField('Product')
    user = OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    status_modes = [
        ('UnVerified', 'UnVerified'),
        ('Verified', 'Verified'),
    ]
    status = models.CharField(
        max_length=11,
        choices = status_modes,
        default = 'UnVerified',
    )







