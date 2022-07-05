from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('common/', include('common.urls')),
    path('forms/', include('forms.urls')),
    path('todo/', include('todo.urls')),
]
