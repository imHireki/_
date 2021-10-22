from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from django.db import models


user = get_user_model()
CASCADE = models.CASCADE
BACKEND_URL = settings.BACKEND_URL


class Icon(models.Model):
    # Image 
    name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='uploads/icons/%Y/%m/')
    slug = models.SlugField(blank=True)

    # User
    user = models.ForeignKey(to=user, on_delete=CASCADE)

    # Time
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
        http://127.0.0.1:8000/media/uploads/icons/2021/01/img.jpeg'
        """
        return f'{BACKEND_URL}{self.image.url}'

    def save(self, *args, **kwargs):
        super(Icon, self).save(*args, **kwargs)
        
        if not self.slug:
            self.slug = self.create_slug(self.slug, self.id)
            self.save()

    def create_slug(slug:str, pk=int):
        _slug = slugify(slug)
        slug_id = f'{_slug}-{pk}' 
        return slug_id

