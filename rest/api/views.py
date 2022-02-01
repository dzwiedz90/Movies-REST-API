from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Director, Actor
from .serializers import GetAllMoviesSerializer, GetAllDirectorsSerializer, GetAllActorsSerializer, \
    CreateMovieSerializer, CreateDirectorSerializer, CreateActorSerializer, UpdateActorSerializer, \
    UpdateMovieSerializer, UpdateDirectorSerializer


class MovieRestApi(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = GetAllMoviesSerializer(movies, many=True)
        return Response({'movies': serializer.data})

    def post(self, request):
        serializer = CreateMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add movie, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            request_id = request.data['id']
            movie = Movie.objects.get(id=request_id)
            serializer = UpdateMovieSerializer(request_id, data=request.data)
            if serializer.is_valid():
                serializer.update(movie, serializer.validated_data)
                return Response({'message': 'Movie modified'},
                                status=status.HTTP_200_OK)
        except Director.DoesNotExist:
            return Response({'message': 'Movie not found'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            request_id = request.data['id']
            movie = Movie.objects.get(id=request_id)
            movie.delete()
            return Response({'message': 'Movie deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)


class DirectorRestApi(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = GetAllDirectorsSerializer(directors, many=True)
        return Response({'directors': serializer.data})

    def post(self, request):
        serializer = CreateDirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Director created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add director, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            request_id = request.data['id']
            director = Director.objects.get(id=request_id)
            serializer = UpdateDirectorSerializer(request_id, data=request.data)
            if serializer.is_valid():
                serializer.update(director, serializer.validated_data)
                return Response({'message': 'Director modified'},
                                status=status.HTTP_200_OK)
        except Director.DoesNotExist:
            return Response({'message': 'Director not found'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            request_id = request.data['id']
            director = Director.objects.get(id=request_id)
            director.delete()
            return Response({'message': 'Director deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except Director.DoesNotExist:
            return Response({'message': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)


class ActorRestApi(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = GetAllActorsSerializer(actors, many=True)
        return Response({'actors': serializer.data})

    def post(self, request):
        serializer = CreateActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Actor created'},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Cant add actor, wrong data'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            request_id = request.data['id']
            actor = Actor.objects.get(id=request_id)
            serializer = UpdateActorSerializer(request_id, data=request.data)
            if serializer.is_valid():
                serializer.update(actor, serializer.validated_data)
                return Response({'message': 'Actor modified'},
                                status=status.HTTP_200_OK)
        except Actor.DoesNotExist:
            return Response({'message': 'Actor not found'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            request_id = request.data['id']
            actor = Actor.objects.get(id=request_id)
            actor.delete()
            return Response({'message': 'Actor deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except Actor.DoesNotExist:
            return Response({'message': 'Actor not found'}, status=status.HTTP_404_NOT_FOUND)


class SingleMovieRestApi(APIView):
    def get(self, request, id):
        movie = Movie.objects.filter(id=self.kwargs['id'])
        serializer = GetAllMoviesSerializer(movie, many=True)
        return Response({'movie': serializer.data})


class SingleActorRestApi(APIView):
    def get(self, request, id):
        actor = Actor.objects.filter(id=self.kwargs['id'])
        serializer = GetAllActorsSerializer(actor, many=True)
        return Response({'actor': serializer.data})


class SingleDirectorRestApi(APIView):
    def get(self, request, id):
        director = Director.objects.filter(id=self.kwargs['id'])
        serializer = GetAllActorsSerializer(director, many=True)
        return Response({'director': serializer.data})
