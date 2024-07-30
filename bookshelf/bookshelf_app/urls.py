# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]