from rest_framework import serializers
from .models import Make, Car, Issue
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class IssueSerializer (serializers.ModelSerializer):
    car = serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = [
            "id",
            "car",
            "title",
            "type"
        ]


class CarSerializer (serializers.ModelSerializer):
    make = serializers.StringRelatedField()
    reports = IssueSerializer(many=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "make",
            "model",
            "reports"
        ]

class CarListSerializer (serializers.ModelSerializer):
    make = serializers.StringRelatedField()

    class Meta:
        ordering = [
            "make",
            "model"
        ]
        model = Car
        fields = [
            "id",
            "make",
            "model"
        ]

class CarCreateSerializer (serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())

    class Meta:
        model = Car
        fields = [
            "id",
            "make",
            "model"
        ]

class CarMakeDetailSerializer (serializers.ModelSerializer):
    class Meta:
        ordering = ["model"]
        model = Car
        fields = [
            "id",
            "model"
        ]


class MakeSerializer (serializers.ModelSerializer):
    cars = CarMakeDetailSerializer(many=True)

    class Meta:
        ordering = ["name"]
        model = Make
        fields = [
            "name",
            "cars"
        ]

class MakeListSerializer (serializers.ModelSerializer):
    class Meta:
        ordering = ["name"]
        model = Make
        fields = [
            "id",
            "name"
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
        fields = [
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
        user = User(password=password, **validated_data)
        user.save()
        return user
