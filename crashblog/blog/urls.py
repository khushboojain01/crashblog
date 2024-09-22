from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'), 

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#the <slug:slug> second slug is from views.py (request, slug)

