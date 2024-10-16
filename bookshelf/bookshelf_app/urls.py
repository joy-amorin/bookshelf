# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #api paths
    path('api/books/', views.api_book_list, name='api_book_list'),
    path('api/books/<int:book_id>/', views.api_book_detail, name='api_book_detail'),
    path('api/books/add/', views.api_add_book, name='api_add_book'),
    path('api/books/delete/<int:book_id>/', views.api_delete_book, name='api_delete_book'),
]
