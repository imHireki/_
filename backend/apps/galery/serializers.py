from rest_framework.serializers import ModelSerializer

from .models import Icon


class IconSerializer(ModelSerializer):
    class Meta:
        model = Icon
        fields = [
            'name',
            'slug',
            'created_at',
            'has_border',
            'has_edit',
            'get_image',
            ]

