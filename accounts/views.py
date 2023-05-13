from rest_framework import generics, permissions

from .serializers import RegisterUserSerializer


# For new users to regiset to the platform
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]
