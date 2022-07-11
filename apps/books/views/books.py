from django.shortcuts import redirect, render

from books.forms import BookForm
from books.forms import BookFormSet
from books.models import Book


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books/pages/index.html', context)


def create(request):
    if request.method == 'POST':
        formset = BookFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('books:index')
        context = {'formset': formset}
        print(formset.errors)
    
    if request.method == 'GET':
        formset = BookFormSet()
        context = {'formset': formset}
    
    return render(request, 'books/pages/create.html', context)