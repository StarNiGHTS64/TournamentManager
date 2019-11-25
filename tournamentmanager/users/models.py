from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_anon = models.BooleanField(default=True)
