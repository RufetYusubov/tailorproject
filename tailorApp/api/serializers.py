from rest_framework import serializers
from tailorApp.models import ClothModel,ContactModel,ContactUsModel,SettingsModel,Mybasket,SizeModel

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

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"

class MybasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mybasket
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = "__all__"
