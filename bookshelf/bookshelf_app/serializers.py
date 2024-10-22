from rest_framework import serializers
from .models import Author, Book, Genre, ReadingPlan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre']

class ReadingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingPlan
        fields = ['id','book', 'pages', 'days', 'pages_per_day']
        read_only_fields = ['pages_per_day']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Para GET
    genre = GenreSerializer()    # Para GET

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre']

    def create(self, validated_data):
        # Extraer los datos del autor y del género de los datos validados
        author_data = validated_data.pop('author')
        genre_data = validated_data.pop('genre')

        # Crear o recuperar el autor y el género
        author, _ = Author.objects.get_or_create(**author_data)
        genre, _ = Genre.objects.get_or_create(**genre_data)

        # Crear el libro con el autor y género asociados
        book = Book.objects.create(author=author, genre=genre, **validated_data)
        return book
