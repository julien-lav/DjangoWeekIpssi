from django.db import models

from django.contrib.auth.models import User

class Resource(models.Model):
    url = models.CharField(max_length=549)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_teacher')
    students = models.ManyToManyField(User, related_name='resource_students')