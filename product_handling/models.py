from django.db import models
from main.models import *
from user_features.models import *

class Cart(models.Model):
    name = models.CharField(max_length=30)
    product = models.ManyToManyField(Product, blank=True)
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

    @property
    def total_price(self):
        queryset = self.product.all().aggregate(
        total_price=models.Sum('price'))
        return queryset["total_price"]

class Order(models.Model):
    cart = OneToOneField(Cart, null=True, on_delete=models.SET_NULL)
    shipping_address = ForeignKey('ShippingAdderss', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.cart.name

class ShippingAdderss(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class Payment(models.Model):
    order = OneToOneField('Order', on_delete=models.SET_NULL, null=True)
    method_modes = [
        ('Bank', 'Bank'),
        ('Cash', 'Cash'),
    ]
    method = models.CharField(
        max_length=11,
        choices = method_modes,
        default = 'Bank',
    )

    status_modes = [
        ('Payed', 'Payed'),
        ('NotPayed', 'NotPayed'),
    ]
    status = models.CharField(
        max_length=11,
        choices = status_modes,
        default = 'NotPayed',
    )


