from django.conf import settings
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["author", "title"]),
        ]

    def __str__(self) -> str:
        return self.title


class Holding(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="holdings")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="holdings")
    purchased_at = models.DateField()

    class Meta:
        unique_together = [("user", "book")]
        ordering = ["-purchased_at", "book__title"]
        indexes = [
            models.Index(fields=["user", "purchased_at"]),
            models.Index(fields=["book"]),
        ]

    def __str__(self) -> str:
        return f"{self.user} → {self.book} ({self.purchased_at})"
