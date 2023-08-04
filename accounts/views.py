from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer

class RegisterView(generics.CreateAPIView):
    """
    API view to register new users to the platform.
    This view allows new users to register by sending a POST request
    with their registration data to the specified endpoint.
    """
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]
