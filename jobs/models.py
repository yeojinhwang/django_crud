from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=20)
    pastJob = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}: {self.pastJob}'