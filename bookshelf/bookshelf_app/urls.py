# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]