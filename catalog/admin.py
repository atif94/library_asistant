from django.contrib import admin
from .models import Author, Book, Holding


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_select_related = ("author",)
    search_fields = ("title", "author__name")
    list_filter = ("author",)


@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "purchased_at")
    list_select_related = ("book", "book__author", "user")
    search_fields = ("user__username", "book__title", "book__author__name")
    list_filter = ("purchased_at", "book__author")
