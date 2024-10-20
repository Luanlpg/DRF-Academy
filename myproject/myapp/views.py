from rest_framework import generics
from rest_framework import viewsets
from .models import Book, Author, Review
from .serializers import BookSerializerMyAPP, ReviewSerializerMyAPP, BookGenericSerializerMyAPP
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsStaffOrReadOnly
'''
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerMyAPP

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerMyAPP

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerMyAPP


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializerMyAPP(books, many=True)   
        return Response(serializer.data)

    def post(self, request):
        serializer = BookGenericSerializerMyAPP(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializerMyAPP(book)   
        return Response(serializer.data)

    def put(self, request, id):
        serializer = BookGenericSerializerMyAPP(data=request.data)
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

'''
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerMyAPP
    permission_classes = [IsStaffOrReadOnly]