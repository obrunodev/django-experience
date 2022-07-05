from django.urls import path

from common.views import common

app_name = 'common'
urlpatterns = [
    path('', common.index, name='index'),
]
