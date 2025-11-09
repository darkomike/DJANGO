from django.db import models
from django.conf import settings


class Follow(models.Model):
    """
    Follow model to track user-to-user following relationships.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Follow relationship
    followerId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
        db_column='followerId',
        help_text="User who is following"
    )
    followingId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followers',
        db_column='followingId',
        help_text="User being followed"
    )
    
    # Cached user information for performance
    followerName = models.CharField(
        max_length=200,
        blank=True,
        help_text="Cached name of the follower"
    )
    followerPhotoURL = models.URLField(
        max_length=500,
        blank=True,
        help_text="Cached photo URL of the follower"
    )
    followingName = models.CharField(
        max_length=200,
        blank=True,
        help_text="Cached name of the user being followed"
    )
    followingPhotoURL = models.URLField(
        max_length=500,
        blank=True,
        help_text="Cached photo URL of the user being followed"
    )
    
    # Timestamp
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-createdAt']
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'
        # Ensure a user can only follow another user once
        unique_together = [['followerId', 'followingId']]
        indexes = [
            models.Index(fields=['-createdAt']),
            models.Index(fields=['followerId', '-createdAt']),
            models.Index(fields=['followingId', '-createdAt']),
        ]
    
    def __str__(self):
        follower_name = self.followerName or self.followerId.username
        following_name = self.followingName or self.followingId.username
        return f"{follower_name} follows {following_name}"
    
    def save(self, *args, **kwargs):
        # Prevent self-following
        if self.followerId == self.followingId:
            raise ValueError("A user cannot follow themselves")
        
        # Auto-populate cached names if not provided
        if not self.followerName:
            self.followerName = (
                f"{self.followerId.first_name} {self.followerId.last_name}".strip() 
                or self.followerId.username
            )
        if not self.followingName:
            self.followingName = (
                f"{self.followingId.first_name} {self.followingId.last_name}".strip() 
                or self.followingId.username
            )
        
        super().save(*args, **kwargs)
    
    @property
    def follower_info(self):
        """Returns follower information dict"""
        return {
            'id': self.followerId.id,
            'name': self.followerName,
            'photoURL': self.followerPhotoURL,
            'username': self.followerId.username,
        }
    
    @property
    def following_info(self):
        """Returns following user information dict"""
        return {
            'id': self.followingId.id,
            'name': self.followingName,
            'photoURL': self.followingPhotoURL,
            'username': self.followingId.username,
        }
