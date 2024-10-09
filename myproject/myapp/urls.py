from django.urls import path
from .views import BookListCreateView, AuthorListCreateView
from .views import BookReviewListCreateView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path(
        "authors/", AuthorListCreateView.as_view(), name="author-list-create"),
    path(
        "reviews/", BookReviewListCreateView.as_view(
        ), name="rewiew-list-create"),
]
