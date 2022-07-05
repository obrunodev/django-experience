from django.shortcuts import render


def index(request):
    return render(request, 'forms/pages/index.html')
