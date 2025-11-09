from django.db import models
from django.conf import settings
from posts.models import Post


class Share(models.Model):
    """
    Share model for tracking post shares across different platforms.
    """
    PLATFORM_CHOICES = [
        ('unknown', 'Unknown'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('reddit', 'Reddit'),
        ('email', 'Email'),
        ('copy_link', 'Copy Link'),
        ('other', 'Other'),
    ]
    
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Relationship to post
    postId = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='shares',
        db_column='postId',
        help_text="The post that was shared"
    )
    
    # User relationship (nullable for guest/anonymous shares)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='shares',
        help_text="User who shared the post. Null for guest shares."
    )
    
    # Platform information
    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES,
        default='unknown',
        help_text="Platform where the post was shared"
    )
    
    # Guest tracking
    isGuest = models.BooleanField(
        default=False,
        help_text="Whether this share is from a guest user"
    )
    
    # Timestamps
    sharedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-sharedAt']
        verbose_name = 'Share'
        verbose_name_plural = 'Shares'
        indexes = [
            models.Index(fields=['-sharedAt']),
            models.Index(fields=['postId', '-sharedAt']),
            models.Index(fields=['user', '-sharedAt']),
            models.Index(fields=['platform', '-sharedAt']),
        ]
    
    def __str__(self):
        user_display = self.user.username if self.user else 'Guest/Anonymous'
        return f"Share by {user_display} on {self.platform} - {self.postId.title}"
    
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
            if not self.sharedAt:
                self.sharedAt = self.createdAt
        
        super().save(*args, **kwargs)
