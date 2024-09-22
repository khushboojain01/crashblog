from django.db import models

class Category(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField() 
    
    class Meta:
        ordering = ('title',  )
        #sorts the categories alphabetically by title
        verbose_name_plural = 'Categories'
        #uses "Categories" as the plural name in the admin interface

    def __str__(self):
        return self.title 
        #category object (1) converted to a string, returns its title

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name ='posts', on_delete=models.CASCADE)
    #connect each post to a category; if the category is deleted, delete the post too
    title = models.CharField(max_length= 255)
    #field for storing the title of the post, limited to 255 characters
    slug = models.SlugField() 
    #URL-friendly version of the title
    intro = models.TextField()
    #for storing longer texts than charfield
    body= models.TextField()
    #contains detail page of the blog
    created_at = models.DateTimeField(auto_now_add=True)
    #tracks time when the post was published
    status = models.CharField(max_length=10, choices = CHOICES_STATUS, default= ACTIVE)

    class Meta:
        ordering = ('-created_at',)
        #sort posts by creation date, newest first
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name ='comments', on_delete=models.CASCADE)
      #connect each comment to a post; if the post is deleted, delete the comment too
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name