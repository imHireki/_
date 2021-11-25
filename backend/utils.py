from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files import File

from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone

from random import randrange
import json
import requests
from io import BytesIO
from os.path import splitext
from random import choice
from time import sleep
from apps.galery.models import Icon, IconImage


def get_img_file(url, img_name): 
    request_img = requests.get(url) 
    
    # Thrown exception if problem with image request
    if request_img.status_code != 200:
        raise Exception(f'status: {request_img.status_code}')
    
    # File management
    bytes_img = request_img.content
    img_io = BytesIO(bytes_img)
    return ImageFile(img_io, name=img_name)

def save_data(data):
    images = data.pop('images')
    icon = Icon.objects.create(**data) 

    for image in images:
        IconImage.objects.create(
            icon=icon,
            image=image
            )

def pm():
    # get data from json 
    file = open('data_3.json', 'r')
    data = json.load(file)
    file.close()
 
    User = get_user_model()
    user = User.objects.filter(id=1).first()

    for key, value in data.items():
        url_images = value['image'] 

        images = []
        for image_url in url_images:
            name = splitext(image_url)[0].split('/')[4:]
            img_name = f"{''.join(name)}.jpg" # Must has file ext
            image = get_img_file(image_url, img_name)
            images.append(image) 

        border = choice([True, False])
        edit = choice([True, False]) # Save data
        
        slug = datetime.strftime(datetime.now(tz=timezone.utc),
                                 '%Y%m%d%H%M%S%f'
                                 )
        save_data({'name': value['title'],
                   'user': user,
                   'has_border': border,
                   'has_edit': edit,
                   'images': images,
                   'slug': slug})

