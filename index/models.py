from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200, null=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=12)
    tel = models.CharField(max_length=12)
    message =models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    