from django.utils import timezone 
from datetime import datetime

from .image import scrap_image


def before_save(data):
    time_now = datetime.now(tz=timezone.utc)
    time_str = datetime.strftime(time_now, '%H%M%S%f')
    datetime_str = datetime.strftime(time_now, '%Y%m%d%H%M%S%f')
   
    #if not data.created_at:
    #   data.created_at = time_now 

    if not data.image_256x:
        data.image, data.image_256x, data.color = scrap_image(
            image=data.image,
            time=time_str
        )
    
    #if not data.name:
    #   data.name = datetime_str

    #if not data.slug:
    #   data.slug = datetime_str

