from django.contrib import admin
from .models import Brand, Product, Category, ProductLine


class ProductLineInlines(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInlines]


admin.site.register(Brand)
admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ProductLine)
