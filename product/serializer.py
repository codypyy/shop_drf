from rest_framework import serializers

from .models import Brand, Category, Product


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = "__all__"
