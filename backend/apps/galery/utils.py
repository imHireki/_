"""
app galery utils
"""
from django.utils.text import slugify


def create_slug(name:str, id:int) -> str:
    """ Create a slug joining `name` and `id` """
    _name = slugify(name)
    slug = f'{_name}-{id}' 
    return slug

