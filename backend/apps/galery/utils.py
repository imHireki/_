"""
app galery utils
"""
from django.core.files.images import ImageFile, File
from django.utils.text import slugify
from django.conf import settings

from io import BytesIO
from PIL import Image
import os
import sys
from base64 import urlsafe_b64encode


def create_slug(name:str, id:int) -> str:
    """ Create a slug joining `name` and `id` """
    _name = slugify(name)
    slug = f'{_name}-{id}' 
    return slug

def resize(image:object) -> tuple:
    """ Shortcut to resize images """
    return ResizeIcon(image).setup_resize()


class ResizeIcon:
    def __init__(self, image:object):
        self.image = image
    
    @property
    def get_original_fp(self):
        """ return full path of the image sent """
        return os.path.join(settings.MEDIA_ROOT, self.image.name)
        
    def get_encoded_names(self, base_name) -> tuple:
        """ return the original and small names encoded """
        original = urlsafe_b64encode((base_name + 'original').encode()
            ).decode()+'.jpg' 

        small = urlsafe_b64encode((base_name + 'small').encode()
            ).decode()+'.jpg'
        return (original, small)
        
    def setup_resize(self):
        """ Manage the path the code will flow to resize """
        # Get names
        names = self.get_encoded_names(os.path.splitext(self.image.name)[0])

        # Get resized images | 70 = 15% loss, 80 = 9% clean
        original = self.resize_img(names[0], original=True, quality=70) 
        
        small = self.resize_img(names[1], size=(200, 200), quality=75)

        # remove original file
        os.remove(self.get_original_fp) 
        return (original, small)

    def resize_img(self, name, quality, size=(), original=False):
        """ Return a resized image """
        with Image.open(self.get_original_fp) as img:

            # Add a white background and convert to RGB 
            if img.mode == 'RGBA':
                white_background = Image.new(
                    'RGBA', img.size, (255, 255, 255)
                    )
                img = Image.alpha_composite(
                    white_background, img
                    ).convert('RGB')
            
            # calc its new size
            if original:
                size = img.size 

            # resize
            img = img.resize(
                size,
                resample=Image.LANCZOS,
                # TODO: chande resample if width > new width
                )

            # save
            img_io = BytesIO()
            img_file = File(img_io, name=name)
            img.save(img_io, format='jpeg', optimize=True, quality=quality)
            return img_file

