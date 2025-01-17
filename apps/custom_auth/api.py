from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import LoginUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class LoginViewSet(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            # breakpoint()
            data = serializer.data
            print(data)
            email = data['email']
            password = data['password']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({"error": "user not found"}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request=request, email=email, password=password)
            if user is None or not user.is_active:
                return Response({"error": "wrong credential."}, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)

            return Response({'refresh': str(refresh),
                             'access': str(refresh.access_token), }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
