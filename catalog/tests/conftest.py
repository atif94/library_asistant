import pytest
from django.contrib.auth import get_user_model
from catalog.models import Author, Book, Holding
from datetime import date

User = get_user_model()

@pytest.fixture
def user(db):
    u = User.objects.create_user(username="alice", password="Secret123!")
    return u

@pytest.fixture
def other_user(db):
    u = User.objects.create_user(username="bob", password="Secret123!")
    return u

@pytest.fixture
def author(db):
    return Author.objects.create(name="George Orwell")

@pytest.fixture
def books(db, author):
    # 12 books to exercise pagination (10/page)
    objs = []
    for i in range(1, 13):
        objs.append(Book.objects.create(title=f"Book {i}", author=author))
    return objs

@pytest.fixture
def holdings(db, user, other_user, books):
    # user holds 2, other_user holds 1 (ensure isolation)
    Holding.objects.create(user=user, book=books[0], purchased_at=date(2025, 1, 1))
    Holding.objects.create(user=user, book=books[1], purchased_at=date(2025, 2, 1))
    Holding.objects.create(user=other_user, book=books[2], purchased_at=date(2025, 3, 1))
