from django.urls import path, include
from .views import BookAPIView, BookDetailAPIView
# from .views import BookListCreateView
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r"reviews", views.ReviewViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookAPIView.as_view(), name="book-list-create"),
    path("books/<int:id>", BookDetailAPIView.as_view(), name="book-delete"),
    # path('reviews/', ReviewListCreateView.as_view(
    # ), name='review-list-create'),
    # path('authors/', AuthorListCreateView.as_view(
    # ), name='author-list-create'),
]
