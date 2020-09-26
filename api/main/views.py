from django.contrib.auth import get_user_model
from django.http import Http404
from .models import Car, Make
from .serializers import * 
from .permissions import *
from rest_framework import mixins
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
import json

User = get_user_model()


class MakeCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Make.objects.all()
    serializer_class = MakeListSerializer


class MakeList(generics.ListAPIView):
    queryset = Make.objects.all().order_by('name')
    serializer_class = MakeListSerializer

class MakeChoices(generics.ListAPIView):
    queryset = Make.objects.all().order_by('name')
    serializer_class = MakeListSerializer
    pagination_class = None

class MakeDetail(generics.RetrieveDestroyAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer

class MakeUpdate(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Make.objects.all()
    serializer_class = MakeListSerializer

class CarCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

class CarList(generics.ListAPIView):
    queryset = Car.objects.all().order_by("model", "make")
    serializer_class = CarListSerializer

class CarChoices(generics.ListAPIView):
    queryset = Car.objects.all().order_by("model", "make")
    serializer_class = CarListSerializer
    pagination_class = None

class CarDetail(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

class CarOwner(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        content = {
            "is_owner": False
        }
        
        try:
            user = car.owners.get(pk=request.user.id)
            content = {
                "is_owner": True
            }
        except User.DoesNotExist:
            content = {
                "is_owner": False
            }

        return Response(content)
    
    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        car.owners.add(request.user.id)
        content = CarSerializer(car).data

        return Response(content)

    def delete(self,request, pk, format=None):
        car = self.get_object(pk)
        car.owners.remove(request.user.id)
        content = CarSerializer(car).data

        return Response(content)

class UserOwnedCars(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = CarListSerializer

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        cars = Car.objects.filter(owners__id=pk)
        page = self.paginate_queryset(cars)
        serializer = self.serializer_class(cars, many=True)

        if page is not None:
            serializer = self.get_paginated_response(serializer.data)

        return Response(serializer.data)


class IssueCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Issue.objects.all()
    serializer_class = IssueCreateSerializer

class IssueList(generics.ListAPIView):
    queryset = Issue.objects.all().order_by("-created_at")
    serializer_class = IssueSerializer

class IssueDetail(generics.RetrieveDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Issue.objects.all()
    serializer_class = IssueCreateSerializer

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

class AuthUserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

class AuthUserUpdatePassword(generics.UpdateAPIView):
    model = User
    serializer_class = UserPasswordSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)