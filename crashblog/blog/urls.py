from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
]
#the <slug:slug> second slug is from views.py (request, slug)

