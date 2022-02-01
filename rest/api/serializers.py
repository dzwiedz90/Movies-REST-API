from rest_framework import serializers

from .models import Actor, Director, Movie


# Actors serializers
class GetAllActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname']


class CreateActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'surname']

        def save(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.save()
            return instance


class UpdateActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'surname']

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.save()
            return instance


# Directors serializers
class GetAllDirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname']


class CreateDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'surname']

        def save(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.save()
            return instance


class UpdateDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'surname']

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.save()
            return instance


# Movie serializers
class GetAllMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_title', 'genre', 'director', 'released', 'cast']


class CreateMovieSerializer(serializers.ModelSerializer):
    director = GetAllDirectorsSerializer(read_only=True, many=True)
    cast = GetAllActorsSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['movie_title', 'genre', 'director', 'released', 'cast']

        def save(self, instance, validated_data):
            instance.movie_title = validated_data.get('movie_title', instance.movie_title)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.director = validated_data.get('director', instance.director)
            instance.released = validated_data.get('released', instance.released)
            instance.cast = validated_data.get('cast', instance.cast)
            instance.save()
            return instance


class UpdateMovieSerializer(serializers.ModelSerializer):
    director = GetAllDirectorsSerializer(read_only=True, many=True)
    cast = GetAllActorsSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['movie_title', 'genre', 'director', 'released', 'cast']

        def update(self, instance, validated_data):
            instance.movie_title = validated_data.get('movie_title', instance.movie_title)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.director = validated_data.get('director', instance.director)
            instance.released = validated_data.get('released', instance.released)
            instance.cast = validated_data.get('cast', instance.cast)
            instance.save()
            return instance
