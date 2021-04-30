from django.contrib import admin
from django.urls import include, path
from .views import base_view, post_view, list_view, comment_view

app_name = 'blogapp'

urlpatterns = [
    path('', base_view.index, name='index'),
    path('post/list', list_view.post_list, name='post_list'),
    path('<int:post_id>/', list_view.detail, name='post_detail'),
    path('post/upload', post_view.post_create, name='post_upload'),
    path('comment/create/post/<int:post_id>/', comment_view.comment_create_post, name='comment_create_post'),
    path('comment/modify/post/<int:comment_id>/', comment_view.comment_modify_post, name='comment_modify_post'),
    path('comment/delete/post/<int:comment_id>/', comment_view.comment_delete_post, name='comment_delete_post'),
]