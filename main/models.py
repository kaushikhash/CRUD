from enum import unique
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    
