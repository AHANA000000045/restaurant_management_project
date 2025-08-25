from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} ({self.status})"


class SalesReport(models.Model):
    date = models.DateField()
    total_orders = models.IntegerField()
    total_sales = models.FloatField()
    top_item = models.CharField(max_length=100)

    def __str__(self):
        return f"Report {self.date} - Total Sales: {self.total_sales}"
