from django.urls import path

from .views import todo

app_name = 'todo'
urlpatterns = [
    path('', todo.index, name='index'),
    # HTMX
    path('create_htmx/', todo.create_htmx, name='create_htmx'),
    path('<int:pk>/update_htmx/', todo.update_htmx, name='update_htmx'),
    path('<int:pk>/delete_htmx/', todo.delete_htmx, name='delete_htmx'),
]
