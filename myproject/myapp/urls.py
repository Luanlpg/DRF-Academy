from django.urls import path
from .views import BookListCreateView, ReviewListCreateView, BookAPIView, BookDetailAPIView #, AuthorListCreateView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list-create'),
    path('books/<int:id>', BookDetailAPIView.as_view(), name='book-delete'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    # path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
]