from rest_framework import serializers
from .models import Make, Car, Issue
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class MakeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = [
            "name"
        ]

class CarSerializer (serializers.ModelSerializer):
    make = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = [
            "id",
            "make",
            "model"
        ]

class IssueSerializer (serializers.ModelSerializer):
    car = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = [
            "car",
            "title",
            "type"
        ]

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff"
        ]

class UserCreateSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields =[
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name"
        ]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = User(password=password,**validated_data)
        user.save()
        return user