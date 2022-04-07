from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Admin(AbstractBaseUser):
    email = models.CharField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name