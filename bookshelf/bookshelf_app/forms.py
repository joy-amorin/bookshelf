from django import forms
from .models import Book, ReadingPlan, Author, Genre

class BookForm(forms.ModelForm):

    authot_name = forms.CharField(max_length=100, label="Author")
    genre_name = forms.CharField(max_length=100, label="Genre")
    class Meta:
        model = Book
        fields = ['title','pages']


class ReadingPlanForm(forms.ModelForm):
    class Meta:
        model = ReadingPlan
        fields = ['book', 'start_date', 'end_date']