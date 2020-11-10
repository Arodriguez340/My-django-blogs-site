from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here
    
class Blog(models.Model):
    '''A model that will store all the blogs.'''

    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    '''A model that will handle all the entries of our blogs.'''

    title = models.CharField(max_length=200)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to='uploads/')
    tags =  TaggableManager(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'entries'

    def __str__(self):
        return self.title


