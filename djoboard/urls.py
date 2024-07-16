from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('jobs/', include('apps.jobs.urls')),
]
