from rest_framework import serializers
from .models import PerevalAdded, PerevalImages, Users

class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'

class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'