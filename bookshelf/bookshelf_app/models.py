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

class ReadingPlan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    pages = models.PositiveBigIntegerField()
    pages_per_day = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    completed_days = models.JSONField(default=list)

    def save(self, *args, **kwargs):

        if self.days > 0:
            self.pages_per_day = self.pages // self.days

        super().save(*args, **kwargs)