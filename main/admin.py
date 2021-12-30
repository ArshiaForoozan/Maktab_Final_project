from django.contrib import admin
from .models import *

@admin.action(description='Mark selected shops as verified')
def make_verified(modeladmin, request, queryset):
    queryset.update(status='Verified')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "image", "status"]
    list_filter = ("name", "status",)

    # def image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.image.url,
    #         width=obj.image.width,
    #         height=obj.image.height,
    #         )
    # )
    search_fields = ("name__startswith", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ("name__startswith", )

@admin.register(OnlineShop)
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ["name", "status",]
    search_fields = ("name__startswith",)
    list_filter = ("name", "status",)
    actions = [make_verified]
