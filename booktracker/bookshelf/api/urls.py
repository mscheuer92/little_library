from django.contrib import admin
from django.urls import path
from bookshelf.views import BookListAPIView, BookDetailAPIView,  BookListByGenreView, BookFilterByAuthorView, BookFilterByTitleAPIView

urlpatterns = [
    path('list/',BookListAPIView.as_view() , name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('title/<str:title>/', BookFilterByTitleAPIView.as_view(), name='book-filter-title'),
    path('author/<str:author>/', BookFilterByAuthorView.as_view(), name='book-filter-author'),
    path('genre/<str:genre>/',BookListByGenreView.as_view(), name='book-filter-genre'),    
]
