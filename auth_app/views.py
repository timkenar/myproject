from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer
from main.models import Visitor, Host

class RegisterVisitorView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        Visitor.objects.create(user=user)
        return response

class RegisterHostView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        Host.objects.create(user=user, name=request.data.get('name', ''))
        return response

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
