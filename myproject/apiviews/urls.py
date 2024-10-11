from django.urls import path
from .views import (
    BookAPIView,
    BookDetailAPIView
)

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list-create'),
    path(
        'books/<int:id>',
        BookDetailAPIView.as_view(),
        name='book-list-create'),
]
