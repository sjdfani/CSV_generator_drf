from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import File_model


class csv_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['password']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_model
        fields = "__all__"
