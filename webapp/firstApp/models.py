from django.db import models

# Create your models here.
class aissm(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.IntegerField()
    region = models.IntegerField()
    charges = models.FloatField()