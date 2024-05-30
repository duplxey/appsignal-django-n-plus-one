from django.http import JsonResponse

from books.models import Book


def index_view(request):
    books = Book.objects.all()
    response = {
        "count": books.count(),
        "results": [{
            "title": book.title,
            "author": book.author.full_name(),
            "summary": book.summary,
            "isbn": book.isbn,
            "published_at": book.published_at,
        } for book in books],
    }
    return JsonResponse(response)

