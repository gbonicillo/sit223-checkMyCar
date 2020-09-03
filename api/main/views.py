from .models import Car
from .serializers import CarSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
import json

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

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