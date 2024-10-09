from rest_framework import generics
from .models import Book, Author, Review
from .serializers import BookSerializer, ReviewSerializer, BookGenericSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializer

    def perform_create(self, serializer):
        author_data = self.request.data.get('author')
        author, created = Author.objects.get_or_create(name=author_data['name'])
        serializer.save(author=author)

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
