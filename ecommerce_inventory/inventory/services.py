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
    def update_product(sku, quantity=None, price=None):
        """Update product quantity and/or price using strategy pattern"""
        product = InventoryManager.get_product(sku)
        
        if quantity is not None:
            quantity_strategy = UpdateQuantityStrategy()
            quantity_strategy.update(product, quantity)
        
        if price is not None:
            price_strategy = UpdatePriceStrategy()
            price_strategy.update(product, price)
        
        return product 


class UpdateStrategy:
    """Interface for update strategies."""
    def update(self, product, value):
        raise NotImplementedError("Update method not implemented.")


class UpdateQuantityStrategy(UpdateStrategy):
    """Concrete strategy for updating product quantity."""
    def update(self, product, value):
        product.quantity = value
        product.save()


class UpdatePriceStrategy(UpdateStrategy):
    """Concrete strategy for updating product price."""
    def update(self, product, value):
        product.price = value
        product.save()