from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm, GenreForm
from .models import Book, Author, Genre, ReadingPlan
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ReadingPlanSerializer
from rest_framework.response import Response

import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

@api_view(['POST'])
def api_add_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        title = remove_accents(serializer.validated_data['title'].lower())
        author_name = remove_accents(serializer.validated_data['author']['author'].lower())

        #verify if the book already exist
        books = Book.objects.all()

        for book in books:
            db_title = remove_accents(book.title.lower())
            db_author = remove_accents(book.author.author.lower())

            if db_title == title and db_author == author_name:
                return Response({'error': f'El libro "{serializer.validated_data["title"]}" de "{serializer.validated_data["author"]["author"]}" ya existe'}, status=400)
                
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
    books = Book.objects.all().order_by('title')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def add_reading_plan(request):
    serializer = ReadingPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def api_reading_plan_list(request):
    plans = ReadingPlan.objects.all()
    serializer = ReadingPlanSerializer(plans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def check_reading_plan(request, book_id):
    try:
        plan = ReadingPlan.objects.filter(book_id=book_id)
        if plan.exists():
            serializer = ReadingPlanSerializer(plan, many=True)
            return Response(serializer.data, status=200)
        else:
             return Response({"message": "Este libro no tiene un plan de lectura asociado"}, status=400)
    except Exception as e:
        return Response({"message": str(e)}, status=500)
       


@api_view(['PATCH'])
def update_progress(request, plan_id):
    try:
        plan = ReadingPlan.objects.get(id=plan_id)
        completed_days = request.data.get('completed_days', [])
        plan.completed_days = completed_days
        plan.save()
        return Response({"message": "Progreso actualizado"}, status=200)
    except ReadingPlan.DoesNotExist:
        return Response({"error":"Plan no encontrado"}, status=404)


