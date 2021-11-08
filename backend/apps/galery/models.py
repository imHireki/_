"""
app galery Models
    - Icon
"""
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from django.db import models

from .utils import create_slug, resize


user = get_user_model()
CASCADE = models.CASCADE
BACKEND_URL = settings.BACKEND_URL
import sys

class Icon(models.Model):
    # Image 
    name = models.CharField(max_length=30)
    user = models.ForeignKey(to=user, on_delete=CASCADE)

    # Image
    image = models.ImageField(upload_to='icons/original/%Y/%m/')
    small_image = models.ImageField(upload_to='icons/small/%Y/%m/', blank=True)
 
    # TODO: get predominant color instead of lazy image
    color = models.CharField(blank=True, max_length=10)

    # Auto
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Attributes
    has_border = models.BooleanField(default=False)
    has_edit = models.BooleanField(default=False) # has_filter ?
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def get_image(self):
        """
        return the url path of the image e.g.,
        http://127.0.0.1:8000/media/icons/2021/01/img.jpeg
        """
        return f'{BACKEND_URL}{self.image.url}'

    def get_small_image(self):
        return f'{BACKEND_URL}{self.small_image.url}'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.image.name

        super().save(*args, **kwargs) 
        
        if not self.small_image:
            self.image, self.small_image = resize(self.image)
            self.save()

        if not self.slug:
            self.slug = create_slug(self.name, self.id)
            self.save()

