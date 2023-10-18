from rest_framework import serializers
from tailorApp.models import ClothModel,ContactModel,ContactUsModel,SizeModel
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer



class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothModel
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = "__all__"

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)



class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
