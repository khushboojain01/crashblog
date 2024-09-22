from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from .forms import CommentForm
from django.shortcuts import redirect

def detail(request, category_slug, slug):  # address for the blog post
    post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)  # to get post based on slug
    # if doesn't get post from slug, throws error 404

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)  # will create a temporary comment for us
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts} )

def search(request):
    searchquery = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter( 
        
        Q(title__icontains=searchquery) | 
        Q(intro__icontains=searchquery) | 
        Q(body__icontains=searchquery)
    )
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': searchquery})

