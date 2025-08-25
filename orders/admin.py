from django.contrib import admin
from .models import Order, SalesReport  # import your models

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'status', 'ordered_at')

@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_orders', 'total_sales', 'top_item')
