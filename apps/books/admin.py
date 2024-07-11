from apps.books.models import Book
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    search_fields = ['title', 'description']
    list_filter = ['status']
