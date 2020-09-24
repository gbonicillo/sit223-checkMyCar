from django.http import HttpResponseBadRequest
from rest_framework import serializers
from .models import Make, Car, Issue
from api.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from textwrap import dedent

User = get_user_model()


class IssueSerializer (serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    type = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Issue
        ordering = [
            "updated_at"
        ]
        fields = [
            "id",
            "car",
            "title",
            "description",
            "type",
            "created_at",
            "updated_at"
        ]
    
    def get_type(self, obj):
        return obj.get_type_display()

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
        model = Car
        fields = [
            "id",
            "model"
        ]

class IssueCreateSerializer (serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    type = serializers.ChoiceField(choices=Issue.ISSUE_TYPE_CHOICES)

    class Meta:
        model = Issue
        fields = [
            "id",
            "car",
            "title",
            "description",
            "type"
        ]
    
    def create(self, validated_data):
        car = Car.objects.get(pk=validated_data["car"].id)
        recipient_list = [owner.email for owner in car.owners.all()]
        report_type = "Issue" if validated_data["type"] == "IS" else "Recall" 

        subject = f"There's a new {report_type} regarding your car {car}"
        message = f"Title: {validated_data['title']}\n\nDescription:\n{validated_data['description']}"

        send_mail(subject, message, EMAIL_HOST_USER, recipient_list,fail_silently = False)

        return Issue.objects.create(**validated_data)

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
        password = make_password(validated_data.pop("password"))
        user = User(password=password, **validated_data)
        user.save()
        return user
    
class UserUpdateSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name"
        ]

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance

class UserPasswordSerializer (serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password"
        ]
