from django.db import models

# Create your models here.

class Author(models.Model):
    '''Book Author Class. Managed only in django admin'''
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"Author: {self.name}"
    

