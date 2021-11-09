"""
app galery tests
"""
from django.test import TestCase
from django.core.files.images import ImageFile
from django.contrib.auth import get_user_model

import os
import sys
from PIL import Image
from io import BytesIO

from .utils import *
from apps.galery.models import Icon

User = get_user_model()


def save_img(size:tuple, form:str, color='RGB'):
    """ Manage the image saving """
    img = Image.new(color, size)
    img.save(
        f'media/tests/{size[0]}x{size[1]}-{color}.{form}',
        form
        )
    img.close()

def create_img():
    """ Manage the creation of the test images """
    sizes = ((100, 50), (256, 256), (1280, 720))
    formats = ('png', 'jpeg')
    colors = ('RGBA', 'RGB')

    for s in range(len(sizes)):
        for f in range(len(formats)):
            if formats[f] == 'png':
                for c in range(len(colors)):
                    save_img(sizes[s], formats[f], colors[c])
            else:
                save_img(sizes[s], formats[f])

def get_img_file(name:str, form:str) -> object:
    """ Get the files from the testdir when they're requested """
    with Image.open(f'media/tests/{name}') as image:
    # with Image.open(f'/home/hireki/Downloads/985055.png') as image:
    # with Image.open(f'/home/hireki/Downloads/985056.jpg') as image:
        img_io = BytesIO()
        image.save(img_io, format=form)
        image_file = ImageFile(img_io, name=name)
    return image_file


class IconTestCase(TestCase):
    def setUp(self):
        # Create the test media dir
        if not os.path.exists('media/tests/'):
            os.makedirs('media/tests/')
        
        # Create the images for the test dir
        create_img() if len(os.listdir('media/tests/')) == 0 else None
        TEST_IMAGES = [name for name in os.listdir('media/tests/')]

        User.objects.create(username='test', password='hsdfah941DSAx')        
        test_user = User.objects.filter(username='test').first()

        for image in TEST_IMAGES:
            n, e = os.path.splitext(image)
            ext = e.replace('.','')
            file = get_img_file(image, ext)
            
            Icon.objects.create(
                user=test_user,
                name=n,
                color='ph',
                image=file
                )
                        
    def test_resize_images(self):
        """
        Test if images are being resized
        """
        for i in Icon.objects.filter(name='test'):
            i = Icon.objects.get(name=n)

            sys.stdout.write(str(
                i.__dict__
                ))

