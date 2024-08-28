from django.db import models

# Create your models here.
class Data(models.Model):
    Task = models.CharField(max_length=100)
    Desc = models.CharField(max_length=500)
    mark = models.IntegerField(default=0)

    def __str__(self):
        return self.Task
    
