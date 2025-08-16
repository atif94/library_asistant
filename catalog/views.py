from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")

@login_required
def my_books(request):
    return render(request, 'catalog/my_books.html')

def book_detail(request,pk):
    return render(request, 'catalog/book_detail.html',{"book": None})

def author_books(request,pk):
    return render(request, 'catalog/author_books.html',{"author": None,"book":[]})

def healthz(request):
    return HttpResponse("OK",status=200)
