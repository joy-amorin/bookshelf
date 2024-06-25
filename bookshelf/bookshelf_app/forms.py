from django import forms
from .models import Book, ReadingPlan, Author, Genre

class BookForm(forms.ModelForm):

    author_name = forms.CharField(max_length=100, label="Author")
    genre_name = forms.CharField(max_length=100, label="Genre")

    class Meta:
        model = Book
        fields = ['title','pages']

    def save(self, commit=True):
        # Override the save method to handle Author and Genre creation.
        book = super().save(commit=False)
        author_name = self.cleaned_data['author_name']
        genre_name = self.cleaned_data['genre_name']

        #get or create the author and genre
        author, created = Author.objects.get_or_create(name=author_name)
        genre, created = Author.objects.get_or_create(name=genre_name)

        #assign author and genre to the book
        book.author = author
        book.genre = genre

        if commit:
            book.save()
        return book 

class ReadingPlanForm(forms.ModelForm):
    class Meta:
        model = ReadingPlan
        fields = ['book', 'start_date', 'end_date']