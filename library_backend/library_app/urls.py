from . import views
from django.urls import path
from .views import BookCreateView, BookListView, BookDeleteView, BookSearchView, BookSearchViewId

urlpatterns = [
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('all-books/', BookListView.as_view(), name='all-books'),
    path('books/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),
    path('book/search/', BookSearchView.as_view(), name='search-book'),
    path('book/<int:pk>/', BookSearchViewId.as_view(), name='search-book-id')
]

