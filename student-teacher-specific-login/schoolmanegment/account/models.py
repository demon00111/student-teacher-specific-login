
# Create your models here
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

POSITION_CHOICES = (

   ('s', 'Student'),
   ('T', 'Teacher')
)


class Profile(models.Model):

   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   gender = models.CharField(choices=GENDER_CHOICES,null=True, max_length=200)
   mobile_number = models.CharField(null=True, max_length=200)
   hobby = models.CharField(null=True, max_length=200)
   dob = models.CharField(null=True, max_length=200)
   user_type = models.CharField(choices=POSITION_CHOICES,null=True, max_length=200)
   caption =  models.CharField(max_length=100,null=True)
   video = models.FileField(upload_to='account/%y',null=True)

   def __str__(self):
      return self.user_type

