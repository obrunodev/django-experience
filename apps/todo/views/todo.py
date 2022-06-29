from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TaskForm
from todo.models import Task


def index(request):
    form = TaskForm()
    tasks = Task.objects.order_by('-id')
    return render(request, 'todo/index.html', {
        'form': form,
        'tasks': tasks
    })


# ========== FUNÇÕES CRUD COM HTMX
def create_htmx(request):
    tasks = Task.objects.order_by('-id')
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa criada!')
    # If form is not valid, render page with errors
    return render(request, 'todo/partials/tasks_component.html', {
        'form': form,
        'tasks': tasks
    })


def delete_htmx(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        try:
            task.delete()
            return render(request, 'todo/partials/tasks_component.html', {
                'tasks': Task.objects.order_by('-id'),
                'form': TaskForm()
            })
        except Exception as e:
            return HttpResponse(f'Erro: {e}')


def update_htmx(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'GET':
        return render(request, 'todo/partials/edit_task.html', {
            'task': task,
            'form': form
        })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return render(request, 'todo/partials/tasks_component.html', {
            'tasks': Task.objects.order_by('-id'),
            'form': TaskForm()
        })
