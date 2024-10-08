from django.contrib import admin
from .models import Post, Category, Comment

class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body', 'owner', 'transaction_hash']
    list_display = ['title', 'slug', 'category', 'created_at', 'status', 'owner', 'transaction_hash', 'block_number']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInLine]
    prepopulated_fields = {'slug': ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title', )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)