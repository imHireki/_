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
    icon = models.ForeignKey(to=Icon,
                             related_name='images',
                             on_delete=models.CASCADE)

    # Original Image. NOTE: Do not modify. Base to all other sizes.
    image = models.ImageField(upload_to='icons/full/%Y/%m/%d')

    image_512x = models.ImageField(upload_to='icons/512x/%Y/%m/%d/', blank=True)
    image_256x = models.ImageField(upload_to='icons/256x/%Y/%m/%d/', blank=True)
    image_128x = models.ImageField(upload_to='icons/128x/%Y/%m/%d/', blank=True)
    image_80x = models.ImageField(upload_to='icons/80x/%Y/%m/%d/', blank=True)

    color = models.CharField(blank=True, max_length=7)

    class Meta:
        ordering = ['-icon']

    def __str__(self):
        return 'Image {} from Icon {}'.format(self.pk, self.icon)
 
    def get_image(self):
        return '{}{}'.format(BACKEND_URL, self.image.url)

    def get_image_512x(self):
        return '{}{}'.format(BACKEND_URL, self.image_512x.url)

    def get_image_256x(self):
        return '{}{}'.format(BACKEND_URL, self.image_256x.url)

    def get_image_128x(self):
        return '{}{}'.format(BACKEND_URL, self.image_128x.url)

    def get_image_80x(self):
        return '{}{}'.format(BACKEND_URL, self.image_80x.url)

    def save(self, *args, **kwargs):
        before_save(self)
        super().save(*args, **kwargs) 

