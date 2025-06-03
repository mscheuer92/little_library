from django.contrib import admin
from django.urls import path
from bookshelf.views import get_book_list, get_book_by_id, get_book_by_title, get_books_by_author

urlpatterns = [

    path('list/', get_book_list, name='book-list'),
    path('<int:pk>/', get_book_by_id, name='book-detail'),
    path('title/<str:title>/', get_book_by_title, name='book-title'),
    path('author/<str:author>/', get_books_by_author, name='book-author')    
]
