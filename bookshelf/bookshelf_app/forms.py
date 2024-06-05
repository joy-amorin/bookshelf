from django import forms
from .models import Book, ReadingPlan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pages']

class ReadingPlanForm(forms.ModelForm):
    class Metea:
        model = ReadingPlan
        fields = ['book', 'start_date', 'end_date']