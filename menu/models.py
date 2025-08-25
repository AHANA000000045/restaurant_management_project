from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
