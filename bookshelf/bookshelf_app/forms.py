from django import forms
from .models import Book, Genre, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','status']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields =['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']