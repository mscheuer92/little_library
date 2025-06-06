from django.contrib import admin
from django.urls import path
from bookshelf.views import BookListAPIView, BookDetailAPIView, BookFilterAPIView
urlpatterns = [

    path('list/',BookListAPIView.as_view() , name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('title/<str:title>/', BookFilterAPIView.as_view(), name='book-filter-title'),
    path('author/<str:author>/', BookFilterAPIView.as_view(), name='book-filter-author'),    
]
