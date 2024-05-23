from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pages = models.IntegerField()

    def __str__(self):
        return self.title

class ReadingPlan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    #def __str__(self):
     #   return f"Plan for {self.book.title}"
    