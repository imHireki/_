from django.contrib.auth import get_user_model
from django.utils import timezone
from django.http import Http404

from rest_framework import serializers

from datetime import datetime

from ..models import Icon, IconImage
import pprint
User = get_user_model()


class UploadIconImageSerializer(serializers.Serializer):
    # IconImage
    image = serializers.ImageField()

    # Icon
    icon = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=30, required=False)
    has_border = serializers.BooleanField(write_only=True)
    has_edit = serializers.BooleanField(write_only=True)
        
    def create(self, validated_data):
        image = validated_data.pop('image')
        user_id = validated_data.pop('user', None)
        icon_id = validated_data.pop('icon', None)
        name = validated_data.get('name', '')

        # User
        if not user_id:
            raise serializers.ValidationError({"detail": "Cum"})
        
        validated_data['user'] = User.objects.filter(
            pk=user_id
            ).first() # TODO: check
        
        # Created at
        time_now = datetime.now(tz=timezone.utc)
        validated_data['created_at'] = time_now
        
        # Slug
        datetime_str = datetime.strftime(time_now, '%Y%m%d%H%M%S%f')
        validated_data['slug'] = datetime_str 

        # Name
        if not name:
            validated_data['name'] = datetime_str
        
        # make an icon or get one
        if not icon_id: 
            icon = Icon.objects.create(**validated_data) 
        else: 
            icon = Icon.objects.filter(pk=icon_id).first()
        
        # Create the object with it
        iconimage = IconImage.objects.create(
            image=image,
            icon=icon
            )
        
        return {'image': iconimage.image}

