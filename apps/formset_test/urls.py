from django.urls import path

from . import views

app_name = 'formset_test'
urlpatterns = [
    path('', views.customers_list, name='customers_list'),
    path('create/', views.customers_create, name='customers_create'),
    path('<int:pk>/delete/', views.customers_delete, name='customers_delete'),
    
    path('<int:customer_id>/create/', views.phone_create, name='phone_create'),
]
