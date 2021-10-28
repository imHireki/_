from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files import File

from django.contrib.auth import get_user_model

from random import randrange
import json
import requests
from io import BytesIO
from os.path import splitext
from random import choice

from apps.galery.models import Icon


def get_img_file(url, img_name): 
    request_img = requests.get(url) 
    
    # Thrown exception if problem with image request
    if request_img.status_code != 200:
        raise Exception(f'status: {request_img.status_code}')
    
    # File management
    bytes_img = request_img.content
    img_io = BytesIO(bytes_img)
    return ImageFile(img_io, name=img_name)
    
def save_data(title, image, border, edit):
    user = get_user_model().objects.get(username='admin')

    icon = Icon(
        user=user,
        name=title,
        image=image,
        has_border=border,
        has_edit=edit
        )

    icon.save()

def populate_model():
    # get data from json 
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
 
    for key, value in data.items():
        # Set data
        title = value['title']
        image_url = value['image']
        
        name  =  splitext(image_url)[0].split('/')[4:]
        img_name = f"{''.join(name)}.jpg" # Must has file ext
        image = get_img_file(image_url, img_name)
       
        border = choice([True, False])
        edit = choice([True, False])
        # Save data
        try:
            save_data(
                title,
                image,
                border,
                edit
                )
        except Exception as e:
            print(e)
 
