"""
app galery Models
    - Icon
"""
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from django.db import models

from .utils.image import scrap_image
from .utils.text import create_slug 

user = get_user_model()
CASCADE = models.CASCADE
BACKEND_URL = settings.BACKEND_URL


class Icon(models.Model):
    # Image 
    name = models.CharField(max_length=30)
    user = models.ForeignKey(to=user, on_delete=CASCADE)

    # Image
    image = models.ImageField(upload_to='icons/full/%Y/%m/%d')
    image_256x = models.ImageField(upload_to='icons/256x/%Y/%m/%d', blank=True)
 
    # TODO: get predominant color instead of lazy image
    color = models.CharField(blank=True, max_length=7)

    # Auto
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField() # handled manually
    
    # Attributes
    has_border = models.BooleanField(default=False)
    has_edit = models.BooleanField(default=False) # has_filter ?
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def get_image(self):
        return f'{BACKEND_URL}{self.image.url}'

    def get_image_256x(self):
        return f'{BACKEND_URL}{self.image_256x.url}'

    def save(self, *args, **kwargs):
        # TODO: add before_save()
         
        from datetime import datetime
        from django.utils import timezone 
    
        time_now = datetime.now(tz=timezone.utc)
        stime_now = datetime.strftime(time_now, '%H%M%S%f')

        self.created_at = time_now 

        if not self.image_256x:
            self.image, self.image_256x, self.color = scrap_image(
                image=self.image, time=stime_now
                )
        
        # TODO: maybe remove it
        if not self.name:
            self.name = self.image.name

        super().save(*args, **kwargs) 
        
        # TODO: Remove the need to save it twice
        if not self.slug:
            self.slug = create_slug(self.name, self.id)
            self.save()
        
