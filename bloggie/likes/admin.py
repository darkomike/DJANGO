from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_display', 'postId', 'isGuest', 'likedAt']
    list_filter = ['isGuest', 'likedAt']
    search_fields = ['user__username', 'postId__title']
    readonly_fields = ['likedAt', 'createdAt']
    ordering = ['-likedAt']
    date_hierarchy = 'likedAt'
    
    def get_user_display(self, obj):
        if obj.user and not obj.isGuest:
            return obj.user.username
        return 'Guest/Anonymous'
    get_user_display.short_description = 'User'
