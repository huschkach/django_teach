from django.db import models
# ORM = object relational mapper

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    studentID = models.IntegerField()
    phone = models.CharField(max_length=20, null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    difficulty = models.IntegerField(null=True)
    question_id = models.AutoField(primary_key=True)

