from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category','created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

# Register your models here.
