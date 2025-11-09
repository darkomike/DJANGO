from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribedAt']
    list_filter = ['subscribedAt']
    search_fields = ['email']
    readonly_fields = ['subscribedAt']
    ordering = ['-subscribedAt']
    date_hierarchy = 'subscribedAt'
