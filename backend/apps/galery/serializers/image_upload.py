from rest_framework.serializers import ModelSerializer
from ..models import Icon, IconImage


class UploadIconSerializer(ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


class UploadIconImageSerializer(ModelSerializer):
    icon = UploadIconSerializer()

    class Meta:
        model = IconImage
        fields = '__all__'

