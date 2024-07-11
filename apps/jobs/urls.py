from apps.jobs import views
from django.urls import path

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='list'),
]
