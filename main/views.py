from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

def hello(request):
    return HttpResponse("Hello, World!")


def books_list(request):
    books = Book.objects.select_related('author').all().order_by('-published_date')
    return render(request, 'main/books_list.html', {'books': books})


def authors_list(request):
    authors = Author.objects.all().order_by('name')
    return render(request, 'main/authors_list.html', {'authors': authors})