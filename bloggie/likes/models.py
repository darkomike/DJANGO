from django.db import models
from django.conf import settings
from posts.models import Post


class Like(models.Model):
    """
    Like model for tracking post likes from users and guests.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Relationship to post
    postId = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        db_column='postId',
        help_text="The post that was liked"
    )
    
    # User relationship (nullable for guest/anonymous likes)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='likes',
        help_text="User who liked the post. Null for guest likes."
    )
    
    # Guest tracking
    isGuest = models.BooleanField(
        default=False,
        help_text="Whether this like is from a guest user"
    )
    
    # Timestamps
    likedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-likedAt']
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        # Ensure a user can only like a post once
        unique_together = [['postId', 'user']]
        indexes = [
            models.Index(fields=['-likedAt']),
            models.Index(fields=['postId', '-likedAt']),
            models.Index(fields=['user', '-likedAt']),
        ]
    
    def __str__(self):
        user_display = self.user.username if self.user else 'Guest/Anonymous'
        return f"Like by {user_display} on {self.postId.title}"
    
    @property
    def user_info(self):
        """
        Returns user information dict similar to the JavaScript structure.
        Returns Anonymous user info if user is null or isGuest is True.
        """
        if self.user and not self.isGuest:
            return {
                'id': self.user.id,
                'name': f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username,
                'email': self.user.email,
                'username': self.user.username,
            }
        else:
            return {
                'id': None,
                'name': 'Anonymous',
                'email': None,
                'username': None,
            }
    
    def save(self, *args, **kwargs):
        # If no user is provided, mark as guest
        if not self.user:
            self.isGuest = True
        
        # Sync timestamps
        if not self.pk:  # Only on creation
            if not self.likedAt:
                self.likedAt = self.createdAt
        
        super().save(*args, **kwargs)
