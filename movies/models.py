from venv import create
from django.db import models
from datetime import datetime

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)    
    class Meta:
        db_table = 'actors'


class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(null=True)   
    running_time = models.IntegerField(default=0)
    actor = models.ManyToManyField(Actor, through='ActorMovie')
    
    class Meta:
        db_table = 'movies'

class ActorMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actormovie'