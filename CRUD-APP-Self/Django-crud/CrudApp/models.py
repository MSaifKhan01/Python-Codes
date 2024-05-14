from django.db import models

# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=265)
    fee = models.IntegerField()



class Teacher(models.Model):
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=265)
    salary = models.IntegerField()




