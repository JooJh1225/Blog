from django.contrib import admin
from django.urls import include, path
from .views import base_view, post_view, list_view

app_name = 'blogapp'

urlpatterns = [
    path('', base_view.index, name='index'),
    path('post/list', list_view.post_list, name='post_list'),
    path('<int:post_id>/', list_view.detail, name='post_detail'),
    path('post/upload', post_view.post_create, name='post_upload'),

]