from django.urls import path
from .views import BookListCreateView, BookDetailView, AuthorListCreateView, AuthorDetailView

urlpatterns = [
    path("api/books/", BookListCreateView.as_view(), name="book-list-create"),
    path("api/books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("api/authors/", AuthorListCreateView.as_view(), name="author-list-create"),
    path("api/authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]
