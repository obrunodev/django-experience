from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('books/', include('books.urls')),
    path('formset_test/', include('formset_test.urls')),
    path('todo/', include('todo.urls')),
    path('user/', include('user.urls')),
]
