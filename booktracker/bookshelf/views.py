from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookshelf.models import Book
from bookshelf.api.serializers import BookSerializer


# View for creating a new book.
@api_view(['POST'])
def create_book(request):
    #serialize the data
    serializer = BookSerializer(data=request.data)
    # if data is valid
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
# View for getting all books.
#/book/list/
@api_view()
def get_book_list(request):
    book = Book.objects.all()
    serializer = BookSerializer(Book.objects.all(), many=True)
    return Response(serializer.data)

# View for getting a specific book by id.
#/book/<id>
@api_view()
def get_book_by_id(request, pk):
    book = Book.objects.get(pk=pk)
    serializer=BookSerializer(book)
    return Response(serializer.data)

#/book/title/title/
@api_view()
def get_book_by_title(request, title):
    book = Book.objects.get(title=title)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# list all books by specific author
@api_view()
def get_books_by_author(request, author):
    book = Book.objects.filter(author=author)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)
