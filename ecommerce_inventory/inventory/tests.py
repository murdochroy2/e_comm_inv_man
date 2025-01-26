import os
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.conf import settings
from inventory.models import Category, Product
from inventory.services import InventoryManager
from decimal import Decimal

class CategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )

    def test_category_creation(self):
        self.assertEqual(str(self.category), "Electronics")
        self.assertEqual(self.category.description, "Electronic items")


class ProductTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )
        self.product = Product.objects.create(
            sku="TEST001",
            name="Test Product",
            price=Decimal("99.99"),
            category=self.category,
            quantity=10
        )

    def test_product_creation(self):
        self.assertEqual(str(self.product), "Test Product")
        self.assertEqual(self.product.price, Decimal("99.99"))
        self.assertEqual(self.product.quantity, 10)
        self.assertEqual(self.product.sku, "TEST001")

    def test_negative_price(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                sku="INVALID001",
                name="Invalid Product",
                price=Decimal("-10.00"),
                category=self.category,
                quantity=5
            )


class InventoryManagerTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )
        self.manager = InventoryManager()

    def test_add_product(self):
        product = self.manager.add_product(
            sku="TEST002",
            name="Test Product",
            price=Decimal("99.99"),
            category=self.category,
            quantity=10
        )
        self.assertEqual(product.quantity, 10)

    def test_remove_product(self):
        product = self.manager.add_product(
            sku="TEST003",
            name="Test Product",
            price=Decimal("99.99"),
            category=self.category
        )
        self.manager.remove_product("TEST003")
        with self.assertRaises(ValueError):
            self.manager.get_product("TEST003") 