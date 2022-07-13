from django.urls import path

from . import views

app_name = 'formset_test'
urlpatterns = [
    path('', views.index, name='index'),
]
