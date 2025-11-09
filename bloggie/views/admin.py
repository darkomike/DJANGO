from django.contrib import admin
from .models import View


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_display', 'postId', 'isGuest', 'viewedAt']
    list_filter = ['isGuest', 'viewedAt']
    search_fields = ['userId__username', 'postId__title']
    readonly_fields = ['viewedAt', 'createdAt']
    ordering = ['-viewedAt']
    date_hierarchy = 'viewedAt'
    
    def get_user_display(self, obj):
        if obj.userId and not obj.isGuest:
            return obj.userId.username
        return 'Guest'
    get_user_display.short_description = 'User'
