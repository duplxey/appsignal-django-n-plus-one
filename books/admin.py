from django.contrib import admin

from books.models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "birth_date"]
    inlines = [BookInline]
    

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_at"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
