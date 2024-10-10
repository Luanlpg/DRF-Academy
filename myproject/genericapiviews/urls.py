from django.urls import path
from .views import (
    BookListCreateView, 
    BookRetrieveUpdateDestroyView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>', BookListCreateView.as_view(), name='book-list-create'),
]