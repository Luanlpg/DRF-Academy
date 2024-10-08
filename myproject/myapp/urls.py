from django.urls import path
from .views import BookListCreateView, ReviewListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]