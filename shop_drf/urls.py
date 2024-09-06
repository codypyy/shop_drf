from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import BrandViewSet, CategoryViewSet, ProductViewSet

route = DefaultRouter()
route.register("brand", BrandViewSet)
route.register("category", CategoryViewSet)
route.register("product", ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls))
]
