"""
app galery serializers
    - IconSerializer
"""
from rest_framework.serializers import ModelSerializer

from .models import Icon

from django.contrib.auth import get_user_model

Owner = get_user_model()


class IconOwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = ['username']

class IconSerializer(ModelSerializer):
    user = IconOwnerSerializer() 

    class Meta:
        model = Icon
        fields = [
            'name',
            'slug',
            'created_at',
            'has_border',
            'has_edit',
            'get_image',
            'get_small_image',
            'user'
            ]

