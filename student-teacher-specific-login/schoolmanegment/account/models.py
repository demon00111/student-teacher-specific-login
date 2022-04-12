
# Create your models here
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

   def __str__(self):
      return f'{self.user_type}'
   # def __str__(self):
   #    print("--------------------------------->>>>Inside __str__")
   #    return self.user

# @receiver(post_save, sender=Profile)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=Profile)
# def save_profile(sender, instance, **kwargs):
#     instance.Profile.save()