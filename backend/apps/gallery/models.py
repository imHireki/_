"""
app gallery Models
    - Icon
"""
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from django.db import models

from .utils.save import before_save

user = get_user_model()
CASCADE = models.CASCADE
BACKEND_URL = settings.BACKEND_URL


class Icon(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(to=user, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField(blank=True)
    has_border = models.BooleanField(default=False)
    has_edit = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def get_icon_url(self):
       return f'icon/{self.slug}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

class IconImage(models.Model):
    icon = models.ForeignKey(
        to=Icon,
        related_name='images',
        on_delete=models.CASCADE,
        ) # Restrict ?
    image = models.ImageField(upload_to='icons/full/%Y/%m/%d')
    image_256x = models.ImageField(upload_to='icons/256x/%Y/%m/%d', blank=True)
    color = models.CharField(blank=True, max_length=7)

    class Meta:
        ordering = ['-icon'] # end up being -created-at
    
    # Add __str__
 
    def get_image(self):
        return f'{BACKEND_URL}{self.image.url}'

    def get_image_256x(self):
        return f'{BACKEND_URL}{self.image_256x.url}'

    def save(self, *args, **kwargs):
        before_save(self)
        super().save(*args, **kwargs) 

