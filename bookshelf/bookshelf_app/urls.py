# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #api paths
    path('books/', views.api_book_list, name='book-list'),
    path('api/books/<int:book_id>/', views.api_book_detail, name='book-detail'),
    path('api/books/add/', views.api_add_book, name='add-book'),
    path('api/books/delete/<int:book_id>/', views.api_delete_book, name='delete-book'),
    path('reading-plans/', views.api_reding_plan_list, name='reading-plan-list'),
    path('reading-plans/add/', views.add_reading_plan, name='add-reading-plan')
]
