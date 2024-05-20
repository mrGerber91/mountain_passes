from rest_framework import serializers
from .models import PerevalAdded, PerevalImages, Users, Coord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'

class LevelSerializer(serializers.Serializer):
    winter = serializers.CharField()
    summer = serializers.CharField()
    autumn = serializers.CharField()
    spring = serializers.CharField()

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'

class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coord = CoordSerializer()

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        user = Users.objects.create(**user_data)
        coord = Coord.objects.create(**coord_data)
        pereval = PerevalAdded.objects.create(user=user, coord=coord, **validated_data)
        return pereval
