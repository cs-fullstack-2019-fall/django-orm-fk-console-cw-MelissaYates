from django.db import models

# Create your models here.
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100, default='Provided no text')
    last_name = models.CharField(max_length=100, default='Provided no text')

    def __str__(self):
         return self.first_name

class Post(models.Model):
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
