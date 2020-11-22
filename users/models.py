from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''A extension of the defaul User model. It will store detailed data about an user.'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    profile_img = models.ImageField(upload_to='profile_img/')
    email = models.EmailField()
    twitter = models.URLField()

# Create your models here.
