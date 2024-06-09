from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.detail, name='post_detail'),
]
#the <slug:slug> second slug is from views.py (request, slug)

