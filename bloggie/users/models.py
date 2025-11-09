from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser with additional profile fields.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('editor', 'Editor'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('banned', 'Banned'),
        ('suspended', 'Suspended'),
    ]
    
    # Unique identifier
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Unique identifier for the user"
    )
    
    # Username is inherited from AbstractUser and is already unique
    # email is inherited but we'll make it required and unique
    email = models.EmailField(
        unique=True,
        help_text="Email address of the user"
    )
    
    # Profile information
    name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Full name of the user"
    )
    displayName = models.CharField(
        max_length=200,
        blank=True,
        help_text="Display name shown publicly"
    )
    bio = models.TextField(
        blank=True,
        max_length=500,
        help_text="User biography"
    )
    
    # Profile images
    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True,
        null=True,
        help_text="User avatar image"
    )
    photoURL = models.URLField(
        max_length=500,
        blank=True,
        help_text="URL to user's photo"
    )
    
    # Social media links
    github = models.URLField(
        max_length=200,
        blank=True,
        help_text="GitHub profile URL"
    )
    linkedin = models.URLField(
        max_length=200,
        blank=True,
        help_text="LinkedIn profile URL"
    )
    twitter = models.URLField(
        max_length=200,
        blank=True,
        help_text="Twitter profile URL"
    )
    website = models.URLField(
        max_length=200,
        blank=True,
        help_text="Personal website URL"
    )
    
    # User role and status
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        help_text="User role in the system"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="User account status"
    )
    
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-createdAt']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['uid']),
            models.Index(fields=['role', 'status']),
            models.Index(fields=['-createdAt']),
        ]
    
    def __str__(self):
        return self.username
    
    @property
    def full_profile(self):
        """Returns complete user profile as a dictionary"""
        return {
            'uid': str(self.uid),
            'username': self.username,
            'name': self.name,
            'displayName': self.displayName or self.username,
            'email': self.email,
            'avatar': self.avatar.url if self.avatar else '',
            'photoURL': self.photoURL,
            'bio': self.bio,
            'github': self.github,
            'linkedin': self.linkedin,
            'twitter': self.twitter,
            'website': self.website,
            'role': self.role,
            'status': self.status,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None,
        }
    
    def save(self, *args, **kwargs):
        # Set displayName to username if not provided
        if not self.displayName:
            self.displayName = self.username
        
        # Set name from first_name and last_name if not provided
        if not self.name and (self.first_name or self.last_name):
            self.name = f"{self.first_name} {self.last_name}".strip()
        
        super().save(*args, **kwargs)
