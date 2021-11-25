from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.utils import timezone

from datetime import datetime

from ..models import Icon, IconImage

User = get_user_model()


class IconUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            ]


class IconImageSerializer(ModelSerializer):
    class Meta:
        model = IconImage
        fields = [
            'id',
            'get_image',
            'get_image_256x',
            ]


class IconSerializer(ModelSerializer):
    user = IconUserSerializer() 
    images = IconImageSerializer(many=True)

    class Meta:
        model = Icon
        fields = [
            'id',
            'name',
            'slug',
            'has_border',
            'has_edit',
            'user',
            'images',
            ]

