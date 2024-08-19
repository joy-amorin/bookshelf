from django import forms
from .models import Book, Author, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

