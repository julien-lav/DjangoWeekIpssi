from django.db import models

from django.contrib.auth.models import User

class Resource(models.Model):
    url = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)