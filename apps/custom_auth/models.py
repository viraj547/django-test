from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from datetime import date


class User(AbstractBaseUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    full_name = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    # def __str__(self):
    #     return "{}".format(self.email)
