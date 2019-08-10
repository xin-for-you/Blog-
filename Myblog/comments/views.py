#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from detail_blog.models import Post

from .models import Comment
from .form import CommentForm

from django.template import RequestContext



def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_list = post.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            form = CommentForm()
        context = {'post': post,'form': form,'comment_list': comment_list}
        return render(request, 'detail_blog/detail.html', context=context)
    return redirect(post)