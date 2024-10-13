from django.contrib import admin
from .models import Author, Book, Genre 

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
