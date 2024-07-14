from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.jobs.models import Job
from apps.jobs.forms import JobForm


def jobs_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'jobs/job_list.html', context)


def jobs_create(request):
    if request.method == 'GET':
        form = JobForm()

    elif request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job added successfully')
            return redirect('jobs:list')

    else:
        return HttpResponse(status=405)

    context = {'form': form}
    return render(request, 'jobs/job_create.html', context)


def jobs_update(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'GET':
        form = JobForm(instance=job)

    elif request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully')
            return redirect('jobs:list')

    else:
        return HttpResponse(status=405)

    context = {
        'form': form,
        'job': job,
        'update': True,
    }
    return render(request, 'jobs/job_create.html', context)


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
