from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from re import split


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """Normalize the email and hash the password."""
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """Set is_staff=True"""
        return self.create_user(email=email, password=password, is_staff=True)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, blank=True)
    # password = ... Referenced on super()
    # last_login = ... Referenced on super()
    is_staff = models.BooleanField(default=False)  # Required on auth/users/

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = split('@', self.email)[0]

        return super().save(*args, **kwargs)
