from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

#class User(AbstractUser):
#    STUDENT = 1
#    TEACHER = 2
#    ROLE_CHOICES = (
#        (STUDENT, 'Student'),
#        (TEACHER, 'Teacher'),
#    )
#    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

     
class Profile(models.Model):
    #STUDENT = 1
    #TEACHER = 2
    #ROLE_CHOICES = (
    #    (STUDENT, 'Student'),
    #    (TEACHER, 'Teacher'),
    #)
    #
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    city = models.CharField(null=True, blank=True, max_length=25)
    firstname = models.CharField(null=True, blank=True, max_length=40)
    lastname = models.CharField(null=True, blank=True, max_length=40)
    phone = PhoneNumberField(null=True, blank=True, unique=True)

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
