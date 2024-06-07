from django.db import models

class Post(models.Model):
    title = models.CharField(max_length= 255)
    #field for storing the title of the post
    slug = models.SlugField() 
    # it is the internet address for title
    intro = models.TextField()
    #for storing longer texts than charfield
    body= models.TextField()
    #contains detail page of the blog
    created_at = models.DateTimeField(auto_now_add=True)
    #tracks time when the post was published

    class Meta:
        ordering = ('-created_at',)