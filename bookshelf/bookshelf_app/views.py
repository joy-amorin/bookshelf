from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm, GenreForm
from .models import Book, Author, Genre
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer
from rest_framework.response import Response

import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

@api_view(['POST'])
def api_add_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['DELETE'])
def api_delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({"message": "Libro Eliminado Exitosamente"}, status=204)
    except Book.DoesNotExist:
        return Response({"error": "Libro no encontrado"}, status=404)
    


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

"""def books_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf_app/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf_app/book_detail.html', {'book': book})"""



