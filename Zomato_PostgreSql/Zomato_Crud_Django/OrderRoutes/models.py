from django.db import models

# Create your models here.
class Order(models.Model):
    foodname=models.CharField()
    name=models.CharField()
    status=models.CharField()
