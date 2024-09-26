from django import forms
from .models import Comment, Post

# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# Blog post form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'slug', 'intro', 'body', 'image', 'status']
        widgets = {
            'category': forms.Select(attrs={'class': 'input'}),
            'title': forms.TextInput(attrs={'class': 'input'}),
            'slug': forms.TextInput(attrs={'class': 'input'}),
            'intro': forms.Textarea(attrs={'class': 'textarea'}),
            'body': forms.Textarea(attrs={'class': 'textarea'}),
            'status': forms.Select(attrs={'class': 'input'}),
        }