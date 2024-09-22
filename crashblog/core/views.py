from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
#since we are not in the same folder as the models file

# Create your views here.
def frontpage(request):
    posts=Post.objects.filter(status = Post.ACTIVE)
    
    return render(request, 'core/frontpage.html',{'posts': posts}) 
    #creates a dictionary here

def aboutpage(request):
    return render(request, 'core/aboutpage.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text),content_type="text/plain")

