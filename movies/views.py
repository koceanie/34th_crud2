from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie

class ActorView(View):
    def get(self, request):
        result=[]
        result = [
            {
                'first_name' : actor.first_name,
                'last_name' : actor.last_name,
                'movie_list' : [{
                    'title' : movie.title
                } for movie in actor.movie_set.all()]
            } for actor in Actor.objects.all()
        ]
        return JsonResponse({'result':result}, status = 200)
    class Meta:
        db_table = "actors"

class MovieView(View):
    def get(self, request):
        result=[]
        result = [
            {
                'title' : movie.title,
                'running_time' : movie.running_time,
                'actor_list' : [{
                    'actor' : actor.first_name
                }for actor in movie.actor.all()]
            } for movie in Movie.objects.all()
        ]
        return JsonResponse({'result':result}, status = 200)
    class Meta:
        db_table = "movies"