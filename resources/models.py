from django.db import models
from django.contrib.auth.models import User
#from users.models import Profile

class Resource(models.Model):
    #students = models.ManyToManyField(Profile, blank=True)
    url = models.CharField(max_length=549)
    user = models.ForeignKey(User, on_delete=models.CASCADE)