from django.contrib.auth import get_user_model
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
import json

User = get_user_model()


class MakeCreate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Make.objects.all()
    serializer_class = MakeListSerializer


class MakeList(generics.ListAPIView):
    queryset = Make.objects.all().order_by('name')
    serializer_class = MakeListSerializer

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


class CarDetail(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

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