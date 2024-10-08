from rest_framework import generics
from .models import Book, Author, Review
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        author_name = self.request.data.get('author.name')
        print(author_name)
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name)
        else:
            raise ValueError("Author data is required")
        serializer.save(author=author)

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer