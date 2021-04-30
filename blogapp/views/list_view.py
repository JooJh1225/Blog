from django.shortcuts import render, get_object_or_404
from ..models import Post

def post_list(request):
    post_index = Post.objects.order_by("-create_date")
    return render(request, "blogapp/post_list.html", {"post_list": post_index})

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "blogapp/post_detail.html", {"post": post})