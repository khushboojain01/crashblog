from django.shortcuts import get_object_or_404, render
from .models import Post

def detail(request, slug):  # address for the blog post
    post = get_object_or_404(Post, slug=slug)  # to get post based on slug
    # if doesn't get post from slug, throws error 404

    return render(request, 'blog/detail.html', {'post': post})
