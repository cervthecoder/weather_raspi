from django.db import models

class Temp(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    time = models.CharField(max_length=5)
    month = models.IntegerField()
