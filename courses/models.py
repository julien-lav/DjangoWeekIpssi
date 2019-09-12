from django.db import models
from django.contrib.auth.models import User

DAY_OF_THE_WEEK_CHOICES = (
    (0, "Lundi"),
    (1, "Mardi"),
    (2, "Mercredi"),
    (3, "Jeudi"),
    (4, "Vendredi"),
    (5, "Samedi"),
    (6, "DImanche"),
)

class Course(models.Model):
    topic = models.CharField(max_length=549)
    dayOfTheWeek = models.PositiveSmallIntegerField(
        choices=DAY_OF_THE_WEEK_CHOICES,
        default=0
    )
    startTime = models.TimeField()
    endTime = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_teacher')
    students = models.ManyToManyField(User, related_name='course_students')