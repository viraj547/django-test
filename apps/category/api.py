from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
