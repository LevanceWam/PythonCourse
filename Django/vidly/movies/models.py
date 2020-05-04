from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # with this if the genre is deleted then all the moves under that genre is deleted as well
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
