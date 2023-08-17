from django.db import models

# Create your models here.

class Menu(models.Model):
    dishname=models.CharField()
    price=models.PositiveIntegerField()
    available=models.CharField()