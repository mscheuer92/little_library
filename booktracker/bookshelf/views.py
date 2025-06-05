from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookshelf.models import Book
from bookshelf.api.serializers import BookSerializer


#/book/list/
@api_view(['GET','POST'])
def get_book_list(request):
    match request.menthod:
        case 'GET':
            book = Book.objects.all()
            # Use serializer
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=200)
        case 'POST':
            serializer = BookSerializer(data=request.data) # get data from user request
            if serializer.is_valid(): # data is considered valid if it's in the correct format
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
    
# View for getting a specific book by id.
#/book/<id>
@api_view(['GET','PUT','DELETE'])
def get_book_by_id(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        match request.method:
            case 'GET':
                serializer=BookSerializer(book)
                return Response(serializer.data, status=200)   
            case 'PUT':
                serializer = BookSerializer(book, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=200)
                else:
                    return Response(serializer.errors, status=400)
            case 'DELETE': 
                book.delete()
                return Response(status=204)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

#/book/title/title/
@api_view()
def get_book_by_title(request, title):
    try:
        book = Book.objects.get(title=title)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Title not found"}, status=404)

# list all books by specific author
@api_view()
def get_books_by_author(request, author):
    try:
        book = Book.objects.filter(author=author)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Author not found"}, status=404)
