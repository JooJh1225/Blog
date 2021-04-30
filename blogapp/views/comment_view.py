from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..models import Post, Comment
from ..forms import PostForm,CommentForm

@login_required(login_url='common:login')
def comment_create_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('blogapp:post_detail', post_id=post.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'blogapp/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_post(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('blogapp:post_detail', post_id=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('blogapp:post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'blogapp/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_post(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('blogapp:post_detail', post_id=comment.post.id)
    else:
        comment.delete()
    return redirect('blogapp:post_detail', post_id=comment.post.id)