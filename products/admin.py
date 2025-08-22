from django.contrib import admin
from .models import Product  # import the correct model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
