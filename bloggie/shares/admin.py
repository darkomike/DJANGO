from django.contrib import admin
from .models import Share


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_display', 'postId', 'platform', 'isGuest', 'sharedAt']
    list_filter = ['platform', 'isGuest', 'sharedAt']
    search_fields = ['user__username', 'postId__title', 'platform']
    readonly_fields = ['sharedAt', 'createdAt']
    ordering = ['-sharedAt']
    date_hierarchy = 'sharedAt'
    
    def get_user_display(self, obj):
        if obj.user and not obj.isGuest:
            return obj.user.username
        return 'Guest/Anonymous'
    get_user_display.short_description = 'User'
