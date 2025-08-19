from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from catalog.models import Author, Book, Holding
from datetime import date

class Command(BaseCommand):
    help = "Seed demo data for Library app"

    def handle(self, *args, **options):
        User = get_user_model()
        user, _ = User.objects.get_or_create(username="demo")
        user.set_password("Demo123!")
        user.save()

        a1, _ = Author.objects.get_or_create(name="Harper Lee")
        a2, _ = Author.objects.get_or_create(name="George Orwell")

        b1, _ = Book.objects.get_or_create(title="To Kill a Mockingbird", author=a1, defaults={"description": "Classic novel."})
        b2, _ = Book.objects.get_or_create(title="Go Set a Watchman", author=a1)
        b3, _ = Book.objects.get_or_create(title="1984", author=a2, defaults={"description": "Dystopian fiction."})
        b4, _ = Book.objects.get_or_create(title="Animal Farm", author=a2)

        Holding.objects.get_or_create(user=user, book=b1, defaults={"purchased_at": date(2024, 5, 12)})
        Holding.objects.get_or_create(user=user, book=b3, defaults={"purchased_at": date(2025, 2, 3)})

        self.stdout.write(self.style.SUCCESS("Seeded demo data. Username: demo / Password: Demo123!"))
