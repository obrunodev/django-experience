from django.contrib import messages
from django.shortcuts import redirect, render

from forms.forms import ProgrammerForm
from forms.models import Programmer


def index(request):
    context = {'programmers': Programmer.objects.order_by('first_name')}
    return render(request, 'forms/pages/index.html', context)


def add_programmer(request):
    if request.method == 'POST':
        form = ProgrammerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Programador cadastrado!')
            return redirect('forms:index')
        context = {'form': form}

    if request.method == 'GET':
        context = {'form': ProgrammerForm()}
    
    return render(request, 'forms/pages/add_programmer.html', context)
