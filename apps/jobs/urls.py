from apps.jobs import views
from django.urls import path

app_name = 'jobs'
urlpatterns = [
    path('', views.jobs_list, name='list'),
    path('create/', views.jobs_create, name='create'),
    path('update/<int:job_id>/', views.jobs_update, name='update'),
    path('delete/<int:job_id>/', views.jobs_delete, name='delete'),
]
