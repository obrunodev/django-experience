from django.urls import path

from books.views import books

app_name = 'books'
urlpatterns = [
    path('', books.index, name='index'),
    path('create/', books.create, name='create'),
]
