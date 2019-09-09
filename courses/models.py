import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models User

class Course(models.Model):
    teacher = models.ForeignKey(Teacher)
    #name = models.CharField()




    


