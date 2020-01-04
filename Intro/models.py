from django.db import models

# Create your models here.
class Introduce(models.Model):
    authors = models.TextField(default = '')
    text = models.TextField(default = '')
    title = models.CharField(max_length = 20, default = 'О нас')
    
    def __str__(self):
        return self.title