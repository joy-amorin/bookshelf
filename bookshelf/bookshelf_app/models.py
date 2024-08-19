from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    