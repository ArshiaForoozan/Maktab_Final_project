from django.contrib import admin
from .models import Cart, Order, ShippingAdderss, Payment

admin.site.register(Cart)
admin.site.register(Order)

@admin.register(ShippingAdderss)
class ShippingAdderssAdmin(admin.ModelAdmin):
    list_display = ["address", "city", "postal_code",]
    search_fields = ("city__startswith",)
    list_filter = ("address", "city",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["order", "status",]
    list_filter = ("status",)