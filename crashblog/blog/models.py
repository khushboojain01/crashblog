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
    def get_absolute_url(self):
        return '/%s/' % self.slug

from django.db import models

class Post(models.Model):
    # Existing fields
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField() 
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    # New fields for proof of ownership
    owner = models.CharField(max_length=255, blank=True, null=True)  # Ethereum address of the owner
    transaction_hash = models.CharField(max_length=255, blank=True, null=True)
    block_number = models.IntegerField(blank=True, null=True)
    blockchain_id = models.IntegerField(null=True, blank=True)
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name ='comments', on_delete=models.CASCADE)
      #connect each comment to a post; if the post is deleted, delete the comment too
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name