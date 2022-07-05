from django.shortcuts import render


def index(request):
    return render(request, 'common/pages/index.html')
