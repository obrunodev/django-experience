from django.http import JsonResponse

from todo.models import Task


def index(request):
    tasks = Task.objects.all()
    data = [task.to_dict_json() for task in tasks]
    return JsonResponse({'data': data})
