from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
    """
    Blog post model with comprehensive fields for content management.
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Core content fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description of the post")
    
    # Categorization
    category = models.CharField(max_length=100, blank=True)
    tags = models.JSONField(default=list, blank=True, help_text="List of tags")
    
    # Authorship and user relationship
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='authored_posts'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    
    # Publishing settings
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published'
    )
    published = models.BooleanField(default=True)
    
    # Media
    coverImage = models.ImageField(
        upload_to='posts/covers/',
        blank=True,
        null=True,
        help_text="Cover image for the post"
    )
    
    # Metadata
    readingTime = models.IntegerField(
        default=0,
        help_text="Estimated reading time in minutes"
    )
    
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-createdAt']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        indexes = [
            models.Index(fields=['-createdAt']),
            models.Index(fields=['slug']),
            models.Index(fields=['status', 'published']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure unique slug
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        
        # Auto-calculate reading time based on content (average 200 words per minute)
        if self.content and self.readingTime == 0:
            word_count = len(self.content.split())
            self.readingTime = max(1, round(word_count / 200))
        
        super().save(*args, **kwargs)
