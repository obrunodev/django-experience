from apps.books.models import Book
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        return Book.published.all()
