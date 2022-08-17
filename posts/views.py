from django.shortcuts import render

# Create your views here.


from posts.models import Post


def first_post(request):
    post = Post.select.first()
     