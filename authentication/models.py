from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)  # PEN as username
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
