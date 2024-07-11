from apps.books import views
from django.urls import path


app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
]
