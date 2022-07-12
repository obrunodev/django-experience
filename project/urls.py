from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user/', include('user.urls')),
    path('books/', include('books.urls')),
    path('todo/', include('todo.urls')),
]
