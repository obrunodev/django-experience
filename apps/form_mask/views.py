from django.shortcuts import get_object_or_404, redirect, render

from form_mask.forms import PersonForm
from form_mask.models import Person


def index(request):
    people = Person.objects.all()
    context = {'people': people}
    return render(request, 'form_mask/pages/person_list.html', context)


def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_mask:index')
        context = {'form': form}
    
    if request.method == 'GET':
        form = PersonForm()
        context = {'form': form}
    
    return render(request, 'form_mask/pages/create.html', context)


def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'GET':
        pass
