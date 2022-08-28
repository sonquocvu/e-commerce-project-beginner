from rest_framework import serializers

from product.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):

    absolute_url = serializers.ReadOnlyField()
    image_url = serializers.ReadOnlyField()
    thumbnail_url = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'description',
            'absolute_url',
            'image_url',
            'thumbnail_url'
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    absolute_url = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'absolute_url',
            'products'
        )