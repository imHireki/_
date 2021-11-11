"""
app galery serializers
    - IconSerializer
"""
from rest_framework.serializers import ModelSerializer

from .models import Icon, IconImage

from django.contrib.auth import get_user_model

Owner = get_user_model()


class IconOwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = ['username']

class IconImageSerializer(ModelSerializer):
    class Meta:
        model = IconImage
        fields = [
            'id',
            'get_image',
            'get_image_256x',
            'color',
            ]

class IconSerializer(ModelSerializer):
    user = IconOwnerSerializer() 
    images = IconImageSerializer(many=True)

    class Meta:
        model = Icon
        fields = [
            'name',
            'slug',
            'created_at',
            'has_border',
            'has_edit',
            'user',
            'images',
            ]

