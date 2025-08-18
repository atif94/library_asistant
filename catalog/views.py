from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.
from django.contrib.auth.views import LoginView

class RememberMeLoginView(LoginView):
    """
    If 'remember' checkbox is unchecked -> expire at browser close.
    If checked -> keep session for SESSION_COOKIE_AGE seconds.
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        remember = self.request.POST.get("remember")
        if not remember:
            # Session ends on browser close
            self.request.session.set_expiry(0)
        else:
            # Respect global SESSION_COOKIE_AGE (e.g., 2 weeks)
            # or set a custom duration here:
            # self.request.session.set_expiry(60 * 60 * 24 * 14)
            pass
        return response

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
