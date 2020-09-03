from rest_framework import serializers
from .models import Make, Car, Issue
from django.contrib.auth.models import User

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
            "username",
            "password",
            "email",
            "first_name",
            "last_name"
        ]