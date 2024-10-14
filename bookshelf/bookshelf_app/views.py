from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm, GenreForm
from .models import Book, Author, Genre
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer
from rest_framework.response import Response

import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        author_form = AuthorForm(request.POST)
        genre_form = GenreForm(request.POST)

        if book_form.is_valid() and author_form.is_valid() and genre_form.is_valid():
            # Get clean data
            author_name = remove_accents(author_form.cleaned_data['author']).lower()
            author, created = Author.objects.get_or_create(author=author_name)

            genre_name = genre_form.cleaned_data['genre']
            genre, created = Genre.objects.get_or_create(genre=genre_name)

            #Chek ig a book with the same author and title already exist, ignoring capitalizacion and accents
            book_title = remove_accents(book_form.cleaned_data['title']).lower()
            existing_book = Book.objects.filter(title__iexact=book_title, author__author__iexact=author_name).first()

            if existing_book:
                messages.error(request, f"El libro '{book_title}' ya existe.")
                return render(request, 'bookshelf_app/add_book.html', {
                    'book_form': book_form,
                    'author_form': author_form,
                    'genre_form': genre_form
                })
            # Create and save the book
            else:
                book = book_form.save(commit=False)
                book.author = author
                book.genre = genre
                book.save()

            messages.success(request, f"El libro fue guardado correctamente")
            return redirect('add_book')
        
    else:
        book_form = BookForm()
        author_form = AuthorForm()
        genre_form = GenreForm()

    return render(request, 'bookshelf_app/add_book.html', {
        'book_form': book_form,
        'author_form': author_form,
        'genre_form': genre_form
    })


def books_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf_app/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf_app/book_detail.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    book.delete()
    messages.success(request, f"El libro {book.title} fue eliminado exitosamente")

    return redirect('books_list')

@api_view(['GET'])
def api_book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)
