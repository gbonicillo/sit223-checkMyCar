from .models import Car
from .serializers import CarSerializer
from rest_framework import mixins
from rest_framework import generics

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer