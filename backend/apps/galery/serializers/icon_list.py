"""
app galery serializers
    - IconSerializer
"""
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.utils import timezone

from datetime import datetime

from ..models import Icon, IconImage

User = get_user_model()


class IconOwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            ]

        extra_kwargs = {
            'username': {
                'validators': [],
                'required': False,
                },
            'id': {
                'read_only': False,
                }
            }

class IconImageSerializer(ModelSerializer):
    class Meta:
        model = IconImage
        fields = [
            'id',
            'image',
            'get_image',
            'get_image_256x',
            'color',
            ]

        # Image just to create
        extra_kwargs = {
            'image': {
                'write_only': True
                }
            }
        
    def create(self, validated_data):   
        # TODO: add support on the serialier to all those fields
        #       maybe different serializers...
        # TODO: remove gap that the code could break
        
        user_id = validated_data.get('user_id', None)
        icon_id = validated_data.get('icon_id', None)
        name = validated_data.get('name', '')
        image = validated_data.get('image', None)

        created_at = datetime.now(tz=timezone.utc)
        user = User.objects.filter(pk=user_id).first()

        if not icon_id:
            # create an icon | name / user / created_at 
            # TODO: add support to has_border... 
            Icon.objects.create(
                name=name, user=user,
                created_at=created_at
                )
            
        # having an icon > get the icon > register the image
        icon_obj = Icon.objects.filter(pk=icon_id).first()
        icon_image = IconImage.objects.create(icon=icon_obj, image=image)
        return icon_image


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

    def create(self, validated_data):
        from datetime import datetime
        from django.utils import timezone
        from sys import stdout

        # Get time
        time_now = datetime.now(tz=timezone.utc)
        time_str = datetime.strftime(time_now, '%H%M%S%f')
        datetime_str = datetime.strftime(time_now, '%Y%m%d%H%M%S%F')
        validated_data['created_at'] = time_now

        # Remove images
        images = validated_data.pop('images')

        # Get User
        uid = validated_data.pop('user').get('id')
        user = User.objects.get(pk=uid) # TODO: check user
        validated_data['user'] = user

        # Create the Icon without any images
        icon = Icon.objects.create(
            **validated_data
            ) 

        # Create the ImageIcon for each image
        IconImage.objects.bulk_create([
            IconImage(
                image=img,
                icon=icon
                )

            for img_dict in images
            for img in img_dict
            ]) 
         
        return icon 

