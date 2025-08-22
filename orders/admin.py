from django.contrib import admin
from .models import Order  # import the correct model

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'ordered_at')
