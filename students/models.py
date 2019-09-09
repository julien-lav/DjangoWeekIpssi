import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models User

class Student(User):
    courses = models.ManyToManyField(Course)

    


