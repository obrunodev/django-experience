from django.views.generic import ListView
from apps.jobs.models import Job


class JobListView(ListView):
    model = Job
