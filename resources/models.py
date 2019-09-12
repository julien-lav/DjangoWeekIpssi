from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Resource(models.Model):
    #students = models.ManyToManyField(Profile, blank=True)
    url = models.CharField(max_length=549)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_teacher')
    courses = models.ManyToManyField(Course, related_name='resource_courses')