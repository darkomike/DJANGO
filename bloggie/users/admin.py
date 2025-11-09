from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User admin with additional fields"""
    
    list_display = ['username', 'email', 'name', 'role', 'status', 'is_staff', 'createdAt']
    list_filter = ['role', 'status', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'name', 'displayName']
    ordering = ['-createdAt']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Profile Information', {
            'fields': ('uid', 'name', 'displayName', 'avatar', 'photoURL', 'bio')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'website')
        }),
        ('Custom Fields', {
            'fields': ('role', 'status', 'createdAt', 'updatedAt')
        }),
    )
    
    readonly_fields = ['uid', 'createdAt', 'updatedAt']
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('email', 'name', 'displayName', 'role', 'status')
        }),
    )
