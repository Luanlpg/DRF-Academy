from rest_framework import generics
from rest_framework import viewsets
from .models import Book, Author, Review
from .serializers import BookSerializer, ReviewSerializer
from .serializers import BookGenericSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializer

<<<<<<< HEAD
    def perform_create(self, serializer):
        author_data = self.request.data.get('author')
        author, created = Author.objects.get_or_create(
            name=author_data['name'])
        serializer.save(author=author)
=======
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializer
>>>>>>> 7db96aeccf1b7cd328445b85f53309f5e2d34e4e

# class ReviewListCreateView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookGenericSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, id):
        serializer = BookGenericSerializer(data=request.data)
        if serializer.is_valid():
            book = Book.objects.get(pk=id)
            book.title = serializer.data['title']
            book.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        books = Book.objects.get(pk=id)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
<<<<<<< HEAD
=======


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializer
>>>>>>> 7db96aeccf1b7cd328445b85f53309f5e2d34e4e
