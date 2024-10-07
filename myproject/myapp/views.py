from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = []
    serializer_class = AuthorSerializer