from django.contrib import admin

from .models import Actor,Director,Movie


class ActorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'movie_title', 'genre', 'released')
    filter_horizontal = ('director', 'cast')

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
