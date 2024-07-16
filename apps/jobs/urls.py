from apps.jobs import views
from django.urls import path

app_name = 'jobs'
urlpatterns = [
    path('', views.JobsListView.as_view(), name='list'),
    path('my-jobs/', views.MyJobsListView.as_view(), name='my_jobs'),
    path('create/', views.jobs_create, name='create'),
    path('update/<int:job_id>/', views.jobs_update, name='update'),
    path('delete/<int:job_id>/', views.jobs_delete, name='delete'),
]
