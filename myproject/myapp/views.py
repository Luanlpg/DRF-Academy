from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_data = self.request.data.get('author')
        author, created = Author.objects.get_or_create(name=author_data['name'])
        serializer.save(author=author)
