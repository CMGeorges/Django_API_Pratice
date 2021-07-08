from django.db import models

# Create your models here.

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10020)
    
    def __str__(self):
        return self.title
    
        