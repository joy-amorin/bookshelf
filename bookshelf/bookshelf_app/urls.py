# bookshelf_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #api paths
    path('', views.api_book_list, name='book-list'),
    path('book-detail/<int:book_id>/', views.api_book_detail, name='book-detail'),
    path('book/add/', views.api_add_book, name='add-book'),
    path('book/delete/<int:book_id>/', views.api_delete_book, name='delete-book'),
    path('reading-plans/', views.api_reading_plan_list, name='reading-plan-list'),
    path('reading-plans/add/', views.add_reading_plan, name='add-reading-plan'),
    path('reading-plans/update-progress/<int:plan_id>/', views.update_progress, name='update_progress'),
    path('reading-plans/check/<int:book_id>/', views.check_reading_plan, name='check_reading_plan'),
]
