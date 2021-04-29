from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import  Paginator
from django.contrib import messages
from ..models import Post
from ..forms import PostForm

@login_required(login_url="common:login")
def post_create(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, "blogapp/post_form.html", {"form": form})