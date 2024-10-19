from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookGenericSerializerViewSet


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookGenericSerializerViewSet
    permission_classes = [IsAuthenticated]
