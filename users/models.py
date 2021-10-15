from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=False)
    birthday = models.DateField(blank=False, default=None, null=True)

    def __str__(self):
        return self.username

