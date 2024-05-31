from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list_view, name="book-list"),
    path("<int:book_id>/", views.book_details_view, name="book-details"),
    path("by-authors/", views.book_by_author_list_view, name="book-by-author-list"),
    path("authors/", views.author_list_view, name="author-list"),
    path("authors/<int:author_id>/", views.author_details_view, name="author-details"),
]
