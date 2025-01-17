from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GenerateDynamicSerializer
from .task import create_dynamic_product

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GenerateDynamicProductViewSet(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = GenerateDynamicSerializer(data=request.data)
        if serializer.is_valid():
            # breakpoint()
            data = serializer.data
            size = data['product_size']
            create_dynamic_product(size)

            return Response({'msg':'success' }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
