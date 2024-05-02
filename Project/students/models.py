from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    studentID = models.IntegerField()

