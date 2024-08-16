from django import forms
from .models import Book, Genre, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','genre', 'pages']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nombre']

class GenreForm(forms.ModelFolrm):
    class Meta:
        model = Genre
        fields = ['nombre']