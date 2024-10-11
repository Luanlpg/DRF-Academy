from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewListCreateView, BookViewSet, AuthorViewSet
# BookAPIView, AuthorListCreateView, BookListCreateView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('review/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('', include(router.urls)),
]
