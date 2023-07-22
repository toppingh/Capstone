from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username