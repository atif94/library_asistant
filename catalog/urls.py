from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_books/', views.my_books, name='my_books'),
    path('books/<int:pk>', views.book_detail, name='book-detail'),
    path("authors/<int:pk>/books/", views.author_books, name="author_books"),
    path('healthz/', views.healthz, name='healthz'),
]