from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Tag(models.Model):
    '''A model that will store all the available tags for certaint blog.'''

    TAGS = (
        ('TECH', 'Technology'),
        ('SCI', 'Science'),
        ('FIN', 'Finace'),
        ('SPT', 'Sport')
    )

    name = models.CharField(max_length=4, choices=TAGS)
    slug = models.SlugField()

    class Meta():
        verbose_name = 'tags'

    def __str__(self):
        return self.name

    
class Blog(models.Model):
    '''A model that will store all the blogs.'''

    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    '''A model that will handle all the entries of our blogs.'''

    title = models.CharField(max_length=200)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'entries'

    def __str__(self):
        return self.title


