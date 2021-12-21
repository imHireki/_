"""
app account models
    - User (AbstractUser) 
"""
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    ...

class User(AbstractBaseUser):
    """
    Main project's User model (AbstractBaseUser)

    ABU_FIELDS = `last_login`, `password`
    """

    # main combination `email` & `password`
    email = models.EmailField(max_length=255, unique=True)

    # username 4 show to others. No needed. Can be made out of the email
    # TODO: fill it with the email
    username = models.CharField(max_length=30, blank=True)

    # TODO: create a relationship to different sizes of icon
    icon = models.ImageField(upload_to=...)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']  # and password


    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
