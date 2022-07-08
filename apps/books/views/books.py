from django.shortcuts import render

from books.forms import BookForm
from books.models import Book


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books/pages/index.html', context)
