from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView

from apps.jobs.models import Job
from apps.jobs.forms import JobForm


class JobsListView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'jobs'
    paginate_by = 10


class MyJobsListView(JobsListView):

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


@login_required
def jobs_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'jobs/job_list.html', context)


@login_required
def jobs_create(request):
    if request.method == 'GET':
        form = JobForm()

    elif request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Job added successfully')
            return redirect('jobs:my_jobs')

    else:
        return HttpResponse(status=405)

    context = {'form': form}
    return render(request, 'jobs/job_form.html', context)


@login_required
def jobs_update(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.user != job.user:
        messages.warning(request, _('You cannot edit this job slot.'))
        return redirect('jobs:list')

    if request.method == 'GET':
        form = JobForm(instance=job)

    elif request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully')
            return redirect('jobs:my_jobs')

    else:
        return HttpResponse(status=405)

    context = {
        'form': form,
        'job': job,
        'update': True,
    }
    return render(request, 'jobs/job_form.html', context)


@login_required
def jobs_delete(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'GET':
        form = JobForm(instance=job)

    elif request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully')
        return redirect('jobs:list')

    else:
        return HttpResponse(status=405)

    context = {
        'form': form,
        'delete': True,
    }
    return render(request, 'jobs/job_delete.html', context)


@login_required
def my_jobs(request):
    """
    Show logged recruiter jobs only.
    """
    if request.method == 'GET':
        jobs = Job.objects.filter(user=request.user)
        context = {'jobs': jobs}
        return render(request, 'jobs/jobs_list.html', context)
