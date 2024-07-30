from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf_app/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf_app/book_detail.html', {'book': book})
