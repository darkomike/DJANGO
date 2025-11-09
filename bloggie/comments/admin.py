from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_display', 'postId', 'text_preview', 'createdAt']
    list_filter = ['createdAt', 'postId']
    search_fields = ['text', 'user__username', 'user__email']
    readonly_fields = ['createdAt', 'updatedAt']
    ordering = ['-createdAt']
    date_hierarchy = 'createdAt'
    
    def get_user_display(self, obj):
        return obj.user.username if obj.user else 'Anonymous'
    get_user_display.short_description = 'User'
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Comment'
