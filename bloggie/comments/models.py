from django.db import models
from django.conf import settings
from posts.models import Post


class Comment(models.Model):
    """
    Comment model for blog posts with user information.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Relationship to post
    postId = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        db_column='postId',
        help_text="The post this comment belongs to"
    )
    
    # User relationship (nullable for anonymous comments)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments',
        help_text="User who created the comment. Null for anonymous comments."
    )
    
    # Comment content
    text = models.TextField(help_text="Comment text content")
    
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-createdAt']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        indexes = [
            models.Index(fields=['-createdAt']),
            models.Index(fields=['postId', '-createdAt']),
        ]
    
    def __str__(self):
        user_display = self.user.username if self.user else 'Anonymous'
        return f"Comment by {user_display} on {self.postId.title}"
    
    @property
    def user_info(self):
        """
        Returns user information dict similar to the JavaScript structure.
        Returns Anonymous user info if user is null.
        """
        if self.user:
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
        # Ensure text is not empty
        if not self.text or not self.text.strip():
            raise ValueError("Comment text cannot be empty")
        super().save(*args, **kwargs)
