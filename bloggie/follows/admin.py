from django.contrib import admin
from .models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_follower', 'get_following', 'createdAt']
    list_filter = ['createdAt']
    search_fields = ['followerId__username', 'followingId__username', 'followerName', 'followingName']
    readonly_fields = ['createdAt']
    ordering = ['-createdAt']
    date_hierarchy = 'createdAt'
    
    def get_follower(self, obj):
        return obj.followerName or obj.followerId.username
    get_follower.short_description = 'Follower'
    
    def get_following(self, obj):
        return obj.followingName or obj.followingId.username
    get_following.short_description = 'Following'
