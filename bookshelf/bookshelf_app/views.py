from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm

# Create your views here.
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf_app/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf_app/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf_app/add_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'bookshelf_app/confirm_delete.html', {'book': book})
        
