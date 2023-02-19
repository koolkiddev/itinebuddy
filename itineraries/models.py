from django.db import models
from sights.models import *
import datetime

class Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    sights = models.ManyToManyField(Sight)

    def get_trip_length(self):
        start = self.start
        end = self.end
        trip_length = end - start

        return trip_length.days
    
    def get_name(self):
        name = "%s in %s days" % (self.destination, self.get_trip_length())
        return name

    def __str__(self):
        return self.get_name()
