from django.http import JsonResponse

from books.models import Book, Author


def book_list_view(request):
    books = Book.objects.all().select_related("author")
    return JsonResponse({
        "count": books.count(),
        "results": [book.to_dict() for book in books],
    })


def book_details_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return JsonResponse(book.to_dict())
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


def book_by_author_list_view(request):
    try:
        authors = Author.objects.all().prefetch_related("books")
        return JsonResponse({
            "count": authors.count(),
            "results": [{
                "author": author.to_dict(),
                "books": [book.to_dict() for book in author.books.all()],
            } for author in authors],
        })
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)


def author_list_view(request):
    authors = Author.objects.all()
    return JsonResponse({
        "count": authors.count(),
        "results": [author.to_dict() for author in authors],
    })


def author_details_view(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        return JsonResponse(author.to_dict())
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)
