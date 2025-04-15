from django.views import generic
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.serializers import RegistrationSerializer, LoginSerializer


class RegisterView(generic.CreateView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = serializer.validated_data['tokens']

        return Response({
            'email': user.email,
            'token': tokens,
        })
