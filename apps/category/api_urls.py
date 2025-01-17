from rest_framework.routers import DefaultRouter
from .api import CategoryViewSet


router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = router.urls
