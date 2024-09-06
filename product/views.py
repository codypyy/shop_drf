from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand, Category, Product
from .serializer import BrandSerializer, CategorySerializer, ProductSerializer

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    def list(self, request):

        serializer_data = BrandSerializer(self.queryset, many=True)
        return Response(serializer_data.data)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):

        serializer_data = CategorySerializer(self.queryset, many=True)
        return Response(serializer_data.data)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):

        serializer_data = ProductSerializer(self.queryset, many=True)
        return Response(serializer_data.data)