from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

class Category(models.Model):
    """
    Category model to group products.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_products(self):
        """
        Retrieves all products in this category.
        """
        return self.products.all()


class Product(models.Model):
    """
    Product model implementing the Observer pattern through signals.
    Products can be observed for stock changes.
    """
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError(_('Price cannot be negative'))
        if self.quantity < 0:
            raise ValidationError(_('Quantity cannot be negative'))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def update_price(self, new_price):
        """Update product price"""
        self.price = new_price
        self.save()

    def update_quantity(self, change_in_quantity):
        """Update product quantity by a given change"""
        new_quantity = self.quantity + change_in_quantity
        if new_quantity < 0:
            raise ValidationError(_('Quantity cannot be negative'))
        self.quantity = new_quantity
        self.save() 