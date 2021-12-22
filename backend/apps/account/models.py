"""
app account models
    - User (AbstractUser) 
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)


class User(AbstractBaseUser):
    """
    Main project's User model (AbstractBaseUser)

    ABU_FIELDS = `last_login`, `password`

    TODO: create a relationship to different sizes of icon
    TODO: use the email to set the username
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
