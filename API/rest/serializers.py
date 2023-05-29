from rest_framework import serializers
from .models import Coords, Level, PerevalAdded, Images, Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'phone')


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('pereval', 'title')


class PerevalAddedSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdded
        exclude = ('id', 'status')

