import collections
import pdb

from rest_framework.test import APITestCase
from rest_framework import status

from .serializers import GetAllMoviesSerializer, GetAllDirectorsSerializer, GetAllActorsSerializer
from .models import Movie, Director, Actor


# Movie API tests
class MovieRestApiTests(APITestCase):

    def setUp(self):
        Director.objects.create(name='Quentin', surname='Tarantino')
        Actor.objects.create(name='John', surname='Travolta')
        Movie.objects.create(movie_title='Django', genre='Western', released='2012')

    def test_create_movie(self):
        response = self.client.post('/api/movies/',
                                    {'movie_title': 'Pulp Fiction', 'genre': 'action', 'director': '1',
                                     'released': '1994',
                                     'cast': '1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.get(id=2).movie_title, 'Pulp Fiction')
        self.assertEqual(Movie.objects.get(id=2).genre, 'action')
        # self.assertEqual(Movie.objects.get().director, '1')
        self.assertEqual(Movie.objects.get(id=2).released, 1994)
        # self.assertEqual(Movie.objects.get().cast, '1')

    def test_create_movie_wrong_data(self):
        response = self.client.post('/api/movies/',
                                    {'movie_titlea': 'Pulp Fiction', 'genre': 'action',
                                     'released': '1994'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant add movie, wrong data'})

    def test_get_movie(self):
        response = self.client.get('/api/movies/1/', format='json')
        movie = Movie.objects.get(id=1)
        serializer = GetAllMoviesSerializer(movie)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data['id'])
        self.assertEqual(response.data[0]['movie_title'], serializer.data['movie_title'])
        self.assertEqual(response.data[0]['genre'], serializer.data['genre'])
        self.assertEqual(response.data[0]['released'], serializer.data['released'])

    def test_get_movie_wrong_id(self):
        response = self.client.get('/api/movies/11/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_all_movies(self):
        Movie.objects.create(movie_title='Titanic', genre='Drama', released='1997')
        response = self.client.get('/api/movies/', format='json')
        movie = Movie.objects.all()
        serializer = GetAllMoviesSerializer(movie, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data[0]['id'])
        self.assertEqual(response.data[0]['movie_title'], serializer.data[0]['movie_title'])
        self.assertEqual(response.data[0]['genre'], serializer.data[0]['genre'])
        self.assertEqual(response.data[0]['released'], serializer.data[0]['released'])
        self.assertEqual(response.data[1]['id'], serializer.data[1]['id'])
        self.assertEqual(response.data[1]['movie_title'], serializer.data[1]['movie_title'])
        self.assertEqual(response.data[1]['genre'], serializer.data[1]['genre'])
        self.assertEqual(response.data[1]['released'], serializer.data[1]['released'])

    def test_update_movie(self):
        response = self.client.put('/api/movies/',
                                   {'id': '1', 'movie_title': 'Pulp Fiction', 'genre': 'action', 'released': '1994'},
                                   format='json')
        movie = Movie.objects.get(id=1)
        serializer = GetAllMoviesSerializer(movie)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Movie modified'})
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer.data['movie_title'], 'Pulp Fiction')
        self.assertEqual(serializer.data['genre'], 'action')
        self.assertEqual(serializer.data['released'], 1994)

    def test_update_movie_wrong_data(self):
        response = self.client.put('/api/movies/',
                                   {'id': '1', 'movie_titlea': 'Pulp Fiction', 'genre': 'action',
                                    'released': '1994'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant modify movie, wrong data'})

    def test_update_movie_wrong_id(self):
        response = self.client.put('/api/movies/',
                                   {'id': '11', 'movie_title': 'Pulp Fiction', 'genre': 'action',
                                    'released': '1994'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Movie not found'})

    def test_delete_movie(self):
        response = self.client.delete('/api/movies/', {'id': '1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'message': 'Movie deleted'})

    def test_delete_movie_wrong_id(self):
        response = self.client.delete('/api/movies/', {'id': '11'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Movie not found'})


# Director API tests
class DirectorRestApiTests(APITestCase):

    def setUp(self):
        Director.objects.create(name='Quentin', surname='Tarantino')
        Actor.objects.create(name='John', surname='Travolta')
        Movie.objects.create(movie_title='Django', genre='Western', released='2012')

    def test_create_director(self):
        response = self.client.post('/api/directors/',
                                    {'name': 'Steven', 'surname': 'Spielberg'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Director.objects.get(id=2).name, 'Steven')
        self.assertEqual(Director.objects.get(id=2).surname, 'Spielberg')

    def test_create_director_wrong_data(self):
        response = self.client.post('/api/directors/',
                                    {'namea': 'Steven', 'surname': 'Spielberg'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant add director, wrong data'})

    def test_get_director(self):
        response = self.client.get('/api/directors/1/', format='json')
        director = Director.objects.get(id=1)
        serializer = GetAllDirectorsSerializer(director)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data['id'])
        self.assertEqual(response.data[0]['name'], serializer.data['name'])
        self.assertEqual(response.data[0]['surname'], serializer.data['surname'])

    def test_get_director_wrong_id(self):
        response = self.client.get('/api/directors/11/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_all_directors(self):
        Director.objects.create(name='Steven', surname='Spielberg')
        response = self.client.get('/api/directors/', format='json')
        director = Director.objects.all()
        serializer = GetAllDirectorsSerializer(director, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data[0]['id'])
        self.assertEqual(response.data[0]['name'], serializer.data[0]['name'])
        self.assertEqual(response.data[0]['surname'], serializer.data[0]['surname'])
        self.assertEqual(response.data[1]['id'], serializer.data[1]['id'])
        self.assertEqual(response.data[1]['name'], serializer.data[1]['name'])
        self.assertEqual(response.data[1]['surname'], serializer.data[1]['surname'])

    def test_update_director(self):
        response = self.client.put('/api/directors/',
                                    {'id': '1', 'name': 'Steven', 'surname': 'Spielberg'}, format='json')
        director = Director.objects.get(id=1)
        serializer = GetAllDirectorsSerializer(director)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Director modified'})
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer.data['name'], 'Steven')
        self.assertEqual(serializer.data['surname'], 'Spielberg')

    def test_update_director_wrong_data(self):
        response = self.client.put('/api/directors/',
                                   {'id': '1', 'namea': 'Steven', 'surname': 'Spielberg'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant modify director, wrong data'})

    def test_update_movie_wrong_id(self):
        response = self.client.put('/api/directors/',
                                   {'id': '11', 'name': 'Steven', 'surname': 'Spielberg'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Director not found'})

    def test_delete_director(self):
        response = self.client.delete('/api/directors/', {'id': '1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'message': 'Director deleted'})

    def test_delete_director_wrong_id(self):
        response = self.client.delete('/api/directors/', {'id': '11'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Director not found'})


# Actor API tests
class ActorRestApiTests(APITestCase):

    def setUp(self):
        Director.objects.create(name='Quentin', surname='Tarantino')
        Actor.objects.create(name='John', surname='Travolta')
        Movie.objects.create(movie_title='Django', genre='Western', released='2012')

    def test_create_actor(self):
        response = self.client.post('/api/actors/',
                                    {'name': 'Leonardo', 'surname': 'DiCaprio'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.get(id=2).name, 'Leonardo')
        self.assertEqual(Actor.objects.get(id=2).surname, 'DiCaprio')

    def test_create_actor_wrong_data(self):
        response = self.client.post('/api/actors/',
                                    {'namea': 'Leonardo', 'surname': 'DiCaprio'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant add actor, wrong data'})

    def test_get_actor(self):
        response = self.client.get('/api/actors/1/', format='json')
        actor = Actor.objects.get(id=1)
        serializer = GetAllActorsSerializer(actor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data['id'])
        self.assertEqual(response.data[0]['name'], serializer.data['name'])
        self.assertEqual(response.data[0]['surname'], serializer.data['surname'])

    def test_get_actor_wrong_id(self):
        response = self.client.get('/api/actors/11/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_all_actors(self):
        Actor.objects.create(name='Leonardo', surname='DiCaprio')
        response = self.client.get('/api/actors/', format='json')
        actor = Actor.objects.all()
        serializer = GetAllActorsSerializer(actor, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], serializer.data[0]['id'])
        self.assertEqual(response.data[0]['name'], serializer.data[0]['name'])
        self.assertEqual(response.data[0]['surname'], serializer.data[0]['surname'])
        self.assertEqual(response.data[1]['id'], serializer.data[1]['id'])
        self.assertEqual(response.data[1]['name'], serializer.data[1]['name'])
        self.assertEqual(response.data[1]['surname'], serializer.data[1]['surname'])

    def test_update_actor(self):
        response = self.client.put('/api/actors/',
                                   {'id': '1', 'name': 'Leonardo', 'surname': 'DiCaprio'}, format='json')
        actor = Actor.objects.get(id=1)
        serializer = GetAllActorsSerializer(actor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Actor modified'})
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer.data['name'], 'Leonardo')
        self.assertEqual(serializer.data['surname'], 'DiCaprio')

    def test_update_actor_wrong_data(self):
        response = self.client.put('/api/actors/',
                                   {'id': '1', 'namea': 'Leonardo', 'surname': 'DiCaprio'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'message': 'Cant modify actor, wrong data'})

    def test_update_actor_wrong_id(self):
        response = self.client.put('/api/actors/',
                                   {'id': '11', 'name': 'Leonardo', 'surname': 'DiCaprio'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Actor not found'})

    def test_delete_actor(self):
        response = self.client.delete('/api/actors/', {'id': '1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'message': 'Actor deleted'})

    def test_delete_actor_wrong_id(self):
        response = self.client.delete('/api/actors/', {'id': '11'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Actor not found'})
