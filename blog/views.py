from typing import Any
from blog.data import posts

from django.shortcuts import render
from django.http import HttpRequest, Http404

# Create your views here.


def post(request: HttpRequest, post_id: int):
    found_post: dict(str, Any) | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não encontrado.')

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context,
    )
def blog(request):
    context = {
        'title': 'Blog',
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )

def example(request):
    context = {
        'text': 'Olá Blog'
    }

    return render(
        request,
        'blog/example.html',
        context,
    )
