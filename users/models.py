from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    info = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.username
