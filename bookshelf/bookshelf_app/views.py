from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm, AuthorForm, GenreForm
# Create your views here.
from .models import Book, Author, Genre

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf_app/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf_app/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        author_form = AuthorForm(request.POST)
        genre_form = GenreForm(request.POST)

        if book_form.is_valid() and author_form.is_valid() and genre_form.is_valid():
            #save or create the author
            author_name = author_form.cleaned_data['name']
            author, created = Author.objects.get_or_create(name=author_name)
            #save or create genre
            genre_name = genre_form.cleaned_data['name']
            genre, created = Genre.objects.get_or_create(name=genre_name)

            #save the book with the author and genre
            book = book_form.save(commit=False)
            book.author = author
            book.genre = genre
            book.save()

            return redirect('books_list')
        
    else:
            book_form = BookForm()
            author_form = AuthorForm()
            genre_form = GenreForm()
    return render(request, 'bookshelf_app/add_book.html', {
            'book_form': book_form,
            'author_form': author_form,
            'genre_form': genre_form
    })
        
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    return render(request, 'bookshelf_app/confirm_delete.html', {'book': book})
        
