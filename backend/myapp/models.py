from django.db import models

# Create your models here.


class Task(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True,default=0)