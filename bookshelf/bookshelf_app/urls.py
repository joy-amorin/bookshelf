# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('book_list/<int:book_id>/', views.book_detail,name='book_detail'),
    path('delete/<int:book_id>/', views.delete_book,name='delete_book')
]