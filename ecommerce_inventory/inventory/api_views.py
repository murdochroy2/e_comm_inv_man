from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from inventory.models import Product, Category
from inventory.serializers import ProductSerializer, CategorySerializer
from inventory.services import InventoryManager
from django.shortcuts import get_object_or_404

class InventoryAPIView(APIView):
    inventory_manager = InventoryManager()

    def get(self, request, pk=None):
        """
        Retrieve a product by its primary key (pk) or all products if no pk is provided.
        """
        if pk:
            product = self.inventory_manager.get_product(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        products = self.inventory_manager.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new product with the provided data.
        """
        name = request.data.get('name')
        price = request.data.get('price')
        sku = request.data.get('sku')
        category = request.data.get('category')
        quantity = request.data.get('quantity', 0)
        category_object = get_object_or_404(Category, name=category)

        try:
            product = self.inventory_manager.add_product(name, price, sku, category_object, quantity)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update an existing product identified by its primary key (pk).
        """
        try:
            product = self.inventory_manager.get_product(pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            
            if serializer.is_valid():
                data = serializer.validated_data
                updated_product = self.inventory_manager.update_product(pk, **data)
                serializer = ProductSerializer(updated_product)
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        """
        Delete a product identified by its primary key (pk).
        """
        try:
            self.inventory_manager.remove_product(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InventoryStockAPIView(APIView):
    inventory_manager = InventoryManager()

    def post(self, request, pk):
        """
        Update the stock quantity of a product identified by its primary key (pk).
        """
        product = self.inventory_manager.get_product(pk)
        quantity = request.data.get('quantity', 0)
        action = request.data.get('action')

        try:
            if action == 'add':
                self.inventory_manager.update_product_quantity(product.sku, quantity)
                message = f'Added {quantity} items to stock'
            elif action == 'remove':
                self.inventory_manager.update_product_quantity(product.sku, quantity)
                message = f'Removed {quantity} items from stock'
            else:
                return Response(
                    {'error': 'Invalid action. Use "add" or "remove"'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return Response({'message': message}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        """
        Retrieve the current stock quantity of a product identified by its primary key (pk).
        """
        product = self.inventory_manager.get_product(pk)
        quantity = self.inventory_manager.check_stock(product)
        return Response({'quantity': quantity}, status=status.HTTP_200_OK)

class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        """
        Retrieve a specific category and its products by primary key (pk) or all categories if no pk is provided.
        """
        if pk:
            # Get specific category and its products
            category = get_object_or_404(Category, pk=pk)
            products = category.get_products()
            product_serializer = ProductSerializer(products, many=True)
            return Response({
                'category': CategorySerializer(category).data,
                'products': product_serializer.data
            })
        
        # Get all categories
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new category with the provided data.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {'error': f'Category with this name already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category identified by its primary key (pk).
        """
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)