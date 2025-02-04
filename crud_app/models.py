from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True) 
    isdelete = models.BooleanField(default=False) 
    image=models.FileField(upload_to='images' ,null=True)