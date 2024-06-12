from django.shortcuts import render

from blog.models import Post
#since we are not in the same folder as the models file

# Create your views here.
def frontpage(request):
    posts=Post.objects.all()
    
    return render(request, 'core/frontpage.html',{'posts': posts}) 
    #creates a dictionary here

def aboutpage(request):
    return render(request, 'core/aboutpage.html')

def search(request, searchquery):
    posts=Post.objects.filter(title__contains=searchquery)
    
    return render(request, 'core/frontpage.html',{'posts': posts}) 
    #creates a dictionary here
