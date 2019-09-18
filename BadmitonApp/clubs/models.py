import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Club(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)
    geo_location_latitude = models.CharField(max_length=200)
    geo_location_longitude = models.CharField(max_length=200)


    def __str__(self):
        return "{}{}".format(self.name,self.location)

    def find_club(name_starts_with):
        clubs = Club.objects.filter(name__starts_with=name_starts_with)

        return clubs

class Session(models.Model):
    session_name = models.CharField(max_length=200)
    starting_time = models.DateTimeField()
    duration = models.DurationField()

    location = models.CharField(max_length=200)
    geo_location_latitude = models.CharField(max_length=200)
    geo_location_longitude = models.CharField(max_length=200)

    capacity = models.IntegerField(default=0)
    player = models.ManyToManyField('Player')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)


    def __str__(self):
        return self.session_name

class Player(models.Model):

    name = models.CharField(max_length=200)
    player_div = models.IntegerField()
    player_club = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Match(models.Model):

    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    court = models.CharField(max_length=200)

    starting_time = models.DateTimeField()
    duration = models.DurationField()


    def __str__(self):
        return self.court
