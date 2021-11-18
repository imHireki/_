from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Icon, IconImage


class UploadIconSerializer(ModelSerializer):
    class Meta:
        model = Icon
        fields = [
            'id',
            'name',
            'created_at',
            'slug',
            'has_border',
            'has_edit',
            ]
        extra_kwargs = {
            'id': {'read_only': False},
            'created_at': {'read_only': False},
            }


class UploadIconImageSerializer(ModelSerializer):
    icon = UploadIconSerializer()

    class Meta:
        model = IconImage
        fields = [
            'image',
            'icon',
            ] 

