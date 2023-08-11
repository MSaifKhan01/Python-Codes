from django.db import models

class FoodItem(models.Model):
    foodname = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    available = models.CharField(max_length=100)


    
