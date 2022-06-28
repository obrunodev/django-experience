from django.urls import path

from .views import todo

app_name = 'todo'
urlpatterns = [
    path('', todo.index, name='index'),
    path('create/', todo.create, name='create'),
    path('<int:pk>/delete/', todo.delete, name='delete'),
    path('<int:pk>/update/', todo.update, name='update'),

    # HTMX
    path('create_htmx/', todo.create_htmx, name='create_htmx'),
]
