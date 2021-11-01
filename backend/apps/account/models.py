"""
app account models
    - User (AbstractUser) 
"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Model to manage User accounts """
    # TODO: Migrate it to AbstractBaseUser
    pass

