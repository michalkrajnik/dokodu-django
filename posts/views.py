from django.shortcuts import render

from posts.models import Post


def first_post(request):
    post = Post.objects.first()
    context = {'first_post': post}
    return render(request, "posts/first_post.html", context)


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}
    return render(request, "posts/posts_list.html", context)


