from django.db import models


class Director(models.Model):
    name = models.CharField('Name', max_length=32)
    surname = models.CharField('Surname', max_length=32)


class Actor(models.Model):
    name = models.CharField('Name', max_length=32)
    surname = models.CharField('Surname', max_length=32)


class Movie(models.Model):
    movie_title = models.CharField('Title', max_length=128)
    genre = models.CharField('Genre', max_length=32)
    director = models.ManyToManyField(Director)
    released = models.IntegerField('Released')
    cast = models.ManyToManyField(Actor)
