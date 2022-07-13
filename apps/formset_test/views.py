from django.shortcuts import render


def index(request):
    return render(request, 'formset_test/pages/index.html')
