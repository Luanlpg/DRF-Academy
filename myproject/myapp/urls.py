from django.urls import path, include   
from rest_framework.routers import DefaultRouter
from .views import (
    BookListCreateView, 
    BookRetrieveUpdateDestroyView, 
    ReviewListCreateView, 
    BookAPIView, 
    BookDetailAPIView,
    BookViewSet
     #, AuthorListCreateView
)

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('', include(router.urls)),
]