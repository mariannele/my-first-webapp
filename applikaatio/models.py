import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone


class Businesstrip(models.Model):
    departure = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance_km = models.IntegerField()
    trip_date = models.DateTimeField('date published')
    def __str__(self):
        tripinfo = self.departure + "-" + self.destination
        return tripinfo

#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  choice_text = models.CharField(max_length=200)
   # votes = models.IntegerField(default=0)
    #def __str__(self):
     #   return self.choice_text
