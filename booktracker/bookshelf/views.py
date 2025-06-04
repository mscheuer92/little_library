from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookshelf.models import Book
from bookshelf.api.serializers import BookSerializer


#/book/list/
@api_view(['GET','POST'])
def get_book_list(request):
    if request.method == 'GET':
        book = Book.objects.all()
        # Use serializer
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data) # get data from user request
        if serializer.is_valid(): # data is considered valid if it's in the correct format
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)
    

# View for getting a specific book by id.
#/book/<id>
@api_view(['GET','PUT','DELETE'])
def get_book_by_id(request, pk):
    match request.method:
        case 'GET':
            book = Book.objects.get(pk=pk)
            serializer=BookSerializer(book)
            return Response(serializer.data)
        case 'PUT':
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        case 'DELETE':
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=204)

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
