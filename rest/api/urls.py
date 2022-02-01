from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('movies/', views.MovieRestApi.as_view(), name='api/movies'),
    path('actors/', views.ActorRestApi.as_view(), name='api/actors'),
    path('directors/', views.DirectorRestApi.as_view(), name='api/directors'),
    path('movies/<int:id>/', views.SingleMovieRestApi.as_view(), name='api/movies/id'),
    path('actors/<int:id>/', views.SingleActorRestApi.as_view(), name='api/actors/id'),
    path('directors/<int:id>/', views.SingleDirectorRestApi.as_view(), name='api/directors/id'),
]
