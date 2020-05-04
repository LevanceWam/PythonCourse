from django.db import models
from django.utils import timezone

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
    # we do not want to call the now method because it will hard code the current time and we do not want that. Instead we want to give it a instance of use calling it that way when we create new movies it will have the correct time
    date_created = models.DateTimeField(default=timezone.now)
