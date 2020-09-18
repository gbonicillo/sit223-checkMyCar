from django.contrib.auth import get_user_model
from .models import Car, Make
from .serializers import * 
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
import json

User = get_user_model()


class MakeCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Make.objects.all()
    serializer_class = MakeListSerializer


class MakeList(generics.ListAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeListSerializer

class MakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer

class CarCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class AuthUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = UserSerializer(request.user)
        content = {
            "user": user.data,
        }

        return Response(content)


class AuthUserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
