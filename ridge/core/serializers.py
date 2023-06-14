import io

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name','first_name', 'additional_name',"phone"]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']
        verbose_name = 'coords'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']
        verbose_name = 'picture'



class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer(required=True)
    coords = CoordsSerializer(required=True)
    level = LevelSerializer(required=True)
    images = ImageSerializer(many=True, required=True)

    class Meta:
        model = Pereval
        fields = ('beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'add_time',
                  'user',
                  'coords',
                  "level",
                  'images',
                  'status',
                  )

