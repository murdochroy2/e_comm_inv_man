from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        # extra_kwargs = {
        #     'description': {'required': False}  # Make description optional
        # }

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()  # This will be used for both input and output

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'price', 'quantity', 'category']

    def to_representation(self, instance):
        # For GET requests - show full category details
        representation = super().to_representation(instance)
        # representation['category'] = CategorySerializer(instance.category).data
        return representation

    def to_internal_value(self, data):
        # For POST/PUT requests - validate category name
        internal_value = super().to_internal_value(data)
        # TODO: Remove this as this api will be called from the frontend
        # category_name = internal_value['category']
        
        # try:
        #     category = Category.objects.get(name=category_name)
        #     internal_value['category'] = category
        # except Category.DoesNotExist:
        #     raise serializers.ValidationError({
        #         'category': f"Category '{category_name}' does not exist. Please create the category first."
        #     })

        if internal_value['quantity'] < 0:
            raise serializers.ValidationError({
                'quantity': 'Quantity must be a positive integer.'
            })

        return internal_value

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        # Get the category by name
        category = Category.objects.get(name=category_name)
        # Create product with the found category
        product = Product.objects.create(category=category, **validated_data)
        return product

    def update(self, instance, validated_data):
        if 'category' in validated_data:
            category_name = validated_data.pop('category')
            try:
                category = Category.objects.get(name=category_name)
                instance.category = category
            except Category.DoesNotExist:
                raise serializers.ValidationError({
                    'category': f"Category '{category_name}' does not exist. Please create the category first."
                })
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance 