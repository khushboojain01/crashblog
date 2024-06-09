from django import forms

from .models import Comment #class name Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        

