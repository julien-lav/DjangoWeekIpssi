from django.db import models

from django.contrib.auth.models import User

class Course(models.Model):
    topic = models.CharField(max_length=549)
    dayOfTheWeek = models.PositiveSmallIntegerField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_teacher')
    students = models.ManyToManyField(User, related_name='course_students')