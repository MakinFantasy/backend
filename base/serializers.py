from rest_framework import serializers
from .models import Category, File, Folder, Tag
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class FileSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = File
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        if len(data['name']) < 3:
            raise serializers.ValidationError('Title should not be less than 3 characters')
        return data
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'