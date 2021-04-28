from django.contrib import admin
from django.urls import include, path
from .views import base_view

app_name = 'blogapp'

urlpatterns = [
    path('', base_view.index, name='index'),
]