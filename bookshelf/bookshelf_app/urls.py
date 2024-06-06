from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
                path("add_book/", views.add_book, name='add_book'),# url to add a book
                path("create_reading_plan/", views.create_reading_plan, name='create_reading_plan'), #url to create a reading plan
]