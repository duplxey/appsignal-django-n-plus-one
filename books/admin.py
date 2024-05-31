from django.contrib import admin

from books.models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "birth_date", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [BookInline]
    

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_at", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
