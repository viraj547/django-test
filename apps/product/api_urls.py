from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api import ProductViewSet,GenerateDynamicProductViewSet


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('generate-dynamic-product/',GenerateDynamicProductViewSet.as_view(),name='generate_dynamic_product')
]
