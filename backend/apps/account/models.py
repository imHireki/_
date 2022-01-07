"""
app account models
    - User (AbstracBaseUser)
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from re import split


class UserManager(BaseUserManager):
    """ Manage the creation of the User objects """

    def create_user(self, email, password=None, **kwargs):
        """ Normalize email and take care of the pass """
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """ The same as create_user, also set is_staff to True """
        return self.create_user(email=email, password=password, is_staff=True)


class User(AbstractBaseUser):
    """
    Main project's User model (AbstractBaseUser)

    ABU_FIELDS = `last_login`, `password`

    is_staff needed to see the auth/users/
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    icon_128x = models.ImageField(upload_to='icons/users/128/%Y/%m/%d',
                                  blank=True, null=True)
    icon_256x = models.ImageField(upload_to='icons/users/256/%Y/%m/%d',
                                  blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    # TODO: check if args & kwargs are needed
    def save(self, *args, **kwargs):

        if not self.username:
            # email part before the @ as username
            self.username = split('@', self.email)[0]

        return super().save(*args, **kwargs)
