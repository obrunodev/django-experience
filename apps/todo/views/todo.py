from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TaskForm
from todo.models import Task


# ========== FUNÇÕES CRUD COMUNS
def index(request):
    form = TaskForm()
    tasks = Task.objects.order_by('-id')
    return render(request, 'todo/index.html', {
        'form': form,
        'tasks': tasks
    })


def create(request):
    form = TaskForm(request.POST or None)
    tasks = Task.objects.all()
    if form.is_valid():
        form.save()
        return redirect('todo:index')
    return render(request, 'todo/index.html', {
        'form': form,
        'tasks': tasks
    })


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:index')
    return render(request, 'todo/delete.html', {'task': task})


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    return render(request, 'todo/update.html', {
        'form': form,
        'task':task
    })


# ========== FUNÇÕES CRUD COM HTMX
def create_htmx(request):
    tasks = Task.objects.order_by('-id')
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa criada!')
        return render(request, 'todo/partials/tasks_component.html', {
            'form': form,
            'tasks': tasks
        })
    # If form is not valid, render page with errors
    return render(request, 'todo/partials/tasks_component.html', {
        'form': form,
        'tasks': tasks
    })
