from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm, ReadingPlanForm
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') #redirect to the list books page after add a book
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def create_reading_plan(request):
    if request.method == 'POST':
        form = ReadingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') #redirect to the list books page after create a reading plan
    else:
        form = ReadingPlanForm()
    return render(request, 'create_reading_plan.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
