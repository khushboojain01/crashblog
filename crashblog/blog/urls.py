
from django.urls import path

from crashblog.sitemaps import CategorySitemap, PostSitemap

from . import views
from crashblog.sitemaps import CategorySitemap, PostSitemap

urlpatterns = [
   path('create/', views.create_blog_post, name='create_blog_post'),  # New route for creating blog post
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'), 
    
    path('verify/<int:post_id>/', views.verify_ownership, name='verify_ownership'),  

] 
#the <slug:slug> second slug is from views.py (request, slug)

