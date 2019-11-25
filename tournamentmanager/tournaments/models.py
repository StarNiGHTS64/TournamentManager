from django.db import models
from django.conf import settings

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField(null=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
