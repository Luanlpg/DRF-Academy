from rest_framework import generics
from .models import Book
from .serializers import BookSerializerGenericView, BookGenericSerializerGenericView


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerGenericView


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerGenericView