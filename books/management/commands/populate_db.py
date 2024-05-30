from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from books.models import Author, Book


class Command(BaseCommand):
    help = "Populates the database with sample data."

    def handle(self, *args, **options):
        fake = Faker()
        author_count = 15
        book_count = 500

        # Create the superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "", "password")

        # Create a few authors
        Author.objects.bulk_create([
            Author(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(),
            ) for _ in range(author_count)
        ])
        authors = Author.objects.all()
        print("Created a few authors.")

        # Create a few books
        Book.objects.bulk_create([
            Book(
                title=fake.sentence(nb_words=6),
                author=authors[fake.random_int(min=0, max=author_count - 1)],
                summary=fake.text(max_nb_chars=512),
                isbn=fake.isbn13(),
                published_at=fake.date_this_century(),
            )
            for _ in range(book_count)
        ])
        print("Created a few books.")
        print("Successfully populated the database.")