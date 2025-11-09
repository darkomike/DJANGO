from django.db import models
from django.conf import settings
from posts.models import Post


class View(models.Model):
    """
    View model for tracking post views from users and guests.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Relationship to post
    postId = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='views',
        db_column='postId',
        help_text="The post that was viewed"
    )
    
    # User relationship (nullable for guest views)
    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='post_views',
        db_column='userId',
        help_text="User who viewed the post. Null for guest views."
    )
    
    # Guest tracking
    isGuest = models.BooleanField(
        default=False,
        help_text="Whether this view is from a guest user"
    )
    
    # Timestamps
    viewedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-viewedAt']
        verbose_name = 'View'
        verbose_name_plural = 'Views'
        indexes = [
            models.Index(fields=['-viewedAt']),
            models.Index(fields=['postId', '-viewedAt']),
            models.Index(fields=['userId', '-viewedAt']),
        ]
    
    def __str__(self):
        user_display = self.userId.username if self.userId else 'Guest'
        return f"View by {user_display} on {self.postId.title}"
    
    def save(self, *args, **kwargs):
        # If no user is provided, mark as guest
        if not self.userId:
            self.isGuest = True
        
        # Sync timestamps
        if not self.pk:  # Only on creation
            if not self.viewedAt:
                self.viewedAt = self.createdAt
        
        super().save(*args, **kwargs)
