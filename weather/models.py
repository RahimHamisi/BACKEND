from django.db import models

# Create your models here.
class Reading(models.Model):
    temperature=models.FloatField()
    humidity=models.FloatField(default=56)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"The time reading for the temprature  of {self.temperature} is {self.time}"
