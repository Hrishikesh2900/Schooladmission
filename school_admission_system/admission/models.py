from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    marks = models.IntegerField(default="0")
    password = models.CharField(max_length=100)
    