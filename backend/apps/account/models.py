"""
app account models
    - User (AbstractUser) 
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        return self.create_user(email=email, password=password, is_staff=True)


class User(AbstractBaseUser):
    """
    Main project's User model (AbstractBaseUser)

    ABU_FIELDS = `last_login`, `password`

    is_staff needed to see the auth/users/

    TODO: create a relationship to different sizes of icon
    TODO: use the email to set the username
    TODO: add icon
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, blank=True)

    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email
