from .models import Book
from rest_framework import serializers
from .serializers import BookSerializerAPIView, BookGenericSerializerAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.tasks import add

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        add.delay(len(books), 1)
        serializer = BookSerializerAPIView(books, many=True)   
        return Response(serializer.data)

    def post(self, request):
        serializer = BookGenericSerializerAPIView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializerAPIView(book)   
        return Response(serializer.data)

    def put(self, request, id):
        serializer = BookGenericSerializerAPIView(data=request.data)
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