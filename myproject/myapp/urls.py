from django.urls import path
from .views import ReviewListCreateView, BookAPIView
# AuthorListCreateView, BookListCreateView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list-create'),
    path('review/', ReviewListCreateView.as_view(), name='review-list-create'),
    # path(
    # 'authors/',
    # AuthorListCreateView.as_view(),
    # name='author-list-create'),
]
