from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    return HttpResponse(movie_id)
