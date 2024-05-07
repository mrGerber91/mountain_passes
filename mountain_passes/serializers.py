from rest_framework import serializers
from .models import PerevalAdded, PerevalImages, Users

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fam = serializers.CharField()
    name = serializers.CharField()
    otc = serializers.CharField()
    phone = serializers.CharField()

class CoordSerializer(serializers.Serializer):
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    height = serializers.CharField()

class LevelSerializer(serializers.Serializer):
    winter = serializers.CharField()
    summer = serializers.CharField()
    autumn = serializers.CharField()
    spring = serializers.CharField()

class ImageSerializer(serializers.Serializer):
    data = serializers.ImageField()
    title = serializers.CharField()

class PerevalAddedSerializer(serializers.Serializer):
    beauty_title = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField()
    add_time = serializers.DateTimeField()
    user = UserSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)