from django.shortcuts import render

from books.forms import BookForm
from books.forms import BookFormSet
from books.models import Book


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books/pages/index.html', context)


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    
    if request.method == 'GET':
        form = BookForm()
        formset = BookFormSet()
        context = {'formset': formset}
    
    return render(request, 'books/pages/create.html', context)