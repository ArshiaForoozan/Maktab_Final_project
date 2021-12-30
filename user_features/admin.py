from django.contrib import admin
from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "email",]
    search_fields = ("email__startswith",)
    list_filter = ("name", "username", "email",)
