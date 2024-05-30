from django.contrib import admin

from books.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "birth_date", "created_at", "updated_at"]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_at", "created_at", "updated_at"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
