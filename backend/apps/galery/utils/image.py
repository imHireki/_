"""
app galery utils
"""
from django.core.files.images import ImageFile, File
from django.conf import settings

from base64 import urlsafe_b64encode
from io import BytesIO
from PIL import Image
import os

from numpy import asarray, product, histogram, argmax
from binascii import hexlify
from scipy import cluster


def scrap_image(image:object) -> tuple:
    """ Shortcut to resize images """
    return ImageScraper(image).setup()

class ImageScraper:
    def __init__(self, image:object):
        self.image = image
        
    def setup(self):
        """ Manage the path the code will flow to resize """
        # Get names
        names = self.get_encoded_names(os.path.splitext(self.image.name)[0])

        original = self.resize_img(names[0], original=True, quality=70) 
        small, img_color = self.resize_img(
            names[1], size=(256, 256), quality=75, color=True
            )

        return (original, small, img_color)

    def get_encoded_names(self, base_name) -> tuple:
        """ return the original and small names encoded """
        original = urlsafe_b64encode((base_name + 'original').encode()
            ).decode()+'.jpg' 

        small = urlsafe_b64encode((base_name + 'small').encode()
            ).decode()+'.jpg'
        return (original, small)
    
    def get_dominant_color(self, image) -> str:
        # Cluster
        ar = asarray(image)
        shape = ar.shape
        ar = ar.reshape(product(shape[:2]), shape[2]).astype(float)

        CLUSTERS = 5 
        codes = cluster.vq.kmeans(ar, CLUSTERS)[0]
        
        # Color frequency
        vecs = cluster.vq.vq(ar, codes)[0] # assign codes
        counts = histogram(vecs, len(codes))[0] # count ocurrences
        index_max = argmax(counts)
        peak = codes[index_max]
        
        # img hex | #000000
        color = str(hexlify(bytearray(int(c) for c in peak)).decode('ascii'))
        return f'#{color}' if len(color) == 6 else f'#{color[:6]}'

    def resize_img(self, name, quality, color=False, size=(), original=False):
        """ Return a resized image """
        with Image.open(self.image) as img:

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
                )

            # save
            img_io = BytesIO()
            img_file = File(img_io, name=name)
            img.save(img_io, format='jpeg', optimize=True, quality=quality)
            
            if color:
                color = self.get_dominant_color(img)
                return img_file, color

            return img_file

