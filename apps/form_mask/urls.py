from django.urls import path

from . import views

app_name = 'form_mask'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
