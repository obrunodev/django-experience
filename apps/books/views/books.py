from django.shortcuts import render


def index(request):
    return render(request, 'books/pages/index.html')
