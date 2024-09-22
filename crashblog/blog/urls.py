
from django.urls import path

from crashblog.sitemaps import CategorySitemap, PostSitemap

from . import views
from crashblog.sitemaps import CategorySitemap, PostSitemap

urlpatterns = [
   
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'), 

] 
#the <slug:slug> second slug is from views.py (request, slug)

