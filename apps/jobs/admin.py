from django.contrib import admin
from apps.jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
