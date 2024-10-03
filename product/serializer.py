from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="name")

    class Meta:
        model = Brand
        fields = ["brand_name"]


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = ["sku", "stock_qty", "price"]


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    # category = CategorySerializer()
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)
    
    class Meta:
        model = Product
        fields = [
            "brand_name",
            "category_name",
            "product_line",
            "name",
            "descriptions",
            "is_digital"
        ]


    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        category_data = validated_data.pop('category')
        product_lines_data = validated_data.pop('product_line')

        brand_obj, created = Brand.objects.get_or_create(name=brand_data["name"])
        category_obj, created = Category.objects.get_or_create(name=category_data["name"])

        product = Product.objects.create(brand=brand_obj, category=category_obj, **validated_data)

        for pld in product_lines_data:
            ProductLine.objects.create(product=product, **pld)
        
        return product


    def update(self, instance, validated_data):
        
        brand_data = validated_data.get('brand', None)
        if brand_data:
            brand_obj, created = Brand.objects.get_or_create(name=brand_data["name"])
            instance.brand = brand_obj
        

        category_data = validated_data.get('category', None)
        if category_data:
            category_obj, created = Category.objects.get_or_create(name=category_data["name"])
            instance.category = category_obj 

        instance.name = validated_data.get("name", instance.name)
        instance.descriptions = validated_data.get("descriptions", instance.descriptions)
        instance.is_digital = validated_data.get("is_digital", instance.is_digital)
        instance.save()

        product_lines_data = validated_data.get('product_line', None)
        if product_lines_data:
            instance.product_line.all().delete()
            for pld in product_lines_data:
                ProductLine.objects.create(product=instance, **pld)

        return instance