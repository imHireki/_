from django.utils import timezone 
from datetime import datetime

from .image import scrap_image


def before_save(instance):
    if not instance.image_256x:
        instance.image, instance.image_256x, instance.color = scrap_image(
            image=instance.image,
            time=datetime.strftime(datetime.now(tz=timezone.utc), '%H%M%S%f')
        )

