from rest_framework.response import Response
from rest_framework.views import APIView
from bookshelf.models import Book
from bookshelf.api.serializers import BookSerializer

class BookListAPIView(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(): # data is considered valid if it's in the correct format
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=200)
        except Book.DoesNotExist:
            return Response({'error': 'Book was not found'}, status=404)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Book.DoesNotExist:
            return Response({'error': 'Book was not found'}, status=404)
        
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=204)

class BookFilterAPIView(APIView):
    def get(self, request, title):
        book = Book.objects.get(title=title)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)

    def get(self, request, author):
        book = Book.objects.get(author=author)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)
