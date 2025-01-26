from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from .models import Product, Category


class InventoryManager:
    """
    Service class implementing the Facade pattern to manage inventory operations.
    """
    
    @staticmethod
    def add_product(name, price, sku, category, quantity=0):
        """Add a new product to inventory"""
        print(f"Price: {price}")
        try:
            product = Product.objects.create(
                name=name,
                price=price,
                sku=sku,
                category=category,
                quantity=quantity
            )
            return product
        except Exception as e:
            raise APIException(f"Failed to add product with SKU {sku}: {str(e)}")

    @staticmethod
    def remove_product(sku):
        """Remove a product from inventory"""
        try:
            product = Product.objects.get(sku=sku)
            product.delete()
        except ObjectDoesNotExist:
            raise APIException(f"Product with SKU {sku} not found")

    @staticmethod
    def get_product(sku):
        """Retrieve a product by SKU"""
        try:
            return Product.objects.get(sku=sku)
        except ObjectDoesNotExist:
            raise APIException(f"Product with SKU {sku} not found")

    @staticmethod
    def get_all_products():
        """Retrieve all products"""
        return Product.objects.all()

    @staticmethod
    def update_product_quantity(sku, quantity):
        """Update product quantity"""
        product = InventoryManager.get_product(sku)
        product.update_quantity(quantity)
        return product 