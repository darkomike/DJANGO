from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message_preview', 'createdAt']
    list_filter = ['createdAt']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['createdAt']
    ordering = ['-createdAt']
    date_hierarchy = 'createdAt'
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'
