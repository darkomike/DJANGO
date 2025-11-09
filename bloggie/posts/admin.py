from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'status', 'published', 'readingTime', 'createdAt', 'user']
    list_filter = ['status', 'published', 'category', 'createdAt']
    search_fields = ['title', 'content', 'excerpt', 'category']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['createdAt', 'updatedAt', 'readingTime']
    ordering = ['-createdAt']
    date_hierarchy = 'createdAt'
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'coverImage')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Authorship', {
            'fields': ('user', 'author')
        }),
        ('Publishing', {
            'fields': ('status', 'published')
        }),
        ('Metadata', {
            'fields': ('readingTime', 'createdAt', 'updatedAt')
        }),
    )
