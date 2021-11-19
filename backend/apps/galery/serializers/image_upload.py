from rest_framework import serializers
from ..models import Icon, IconImage


class UploadIconImageSerializer(serializers.Serializer):
    iconimage_image = serializers.ImageField()

    icon_id = serializers.IntegerField(required=False)
    icon_user_id = serializers.IntegerField(required=False)

    icon_name = serializers.CharField(max_length=30, required=False)
    icon_has_border = serializers.BooleanField()
    icon_has_edit = serializers.BooleanField()
        
    def create(self, validated_data):
        # created_at = datetime.now(tz=timezone.utc)
        # time_str = datetime.strftime(time_now, '%H%M%S%f')
        # datetime_str = datetime.strftime(time_now, '%Y%m%d%H%M%S%F')
        ...

