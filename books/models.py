from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(to=Author, related_name="books", on_delete=models.CASCADE)
    summary = models.TextField(max_length=512, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, help_text="ISBN-13")
    published_at = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.to_dict(),
            "summary": self.summary,
            "isbn": self.isbn,
            "published_at": self.published_at,
        }

    def __str__(self):
        return f"{self.author}: {self.title}"
