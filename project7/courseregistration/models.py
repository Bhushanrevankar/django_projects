

from django.db import models

#Create your models here.

class Student(models. Model):
    name = models.CharField(max_length=30)
    usn= models. CharField(max_length=10)

    def str(self) -> str: 
        return self.name

class Course(models. Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=8)
    enrolment = models.ManyToManyField(Student)

def _str_ (self) -> str:
    return self.name