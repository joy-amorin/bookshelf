from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
                path("add/", views.add_book, name='add_book'),# url to add a book
                path("plan/", views.create_reading_plan, name='create_reading_plan'), #url to create a reading plan
                path("booklist/", views.book_list, name='book_list'), #url to book list 
]