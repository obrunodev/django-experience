from django.urls import path
from apps.forms.views import forms

from forms.views import forms

app_name = 'forms'
urlpatterns = [
    path('', forms.index, name='index'),
]
