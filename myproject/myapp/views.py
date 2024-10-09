from rest_framework import generics  # type: ignore
from .models import Author, Book, BookReview
from .serializers import BookGenericSerializer, BookReviewSerializer
from .serializers import AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializer

    def perform_create(self, serializer):
        author_data = self.request.data.get("author")
        author, created = Author.objects.get_or_create(
            name=author_data["name"])
        serializer.save(author=author)


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookReviewListCreateView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
