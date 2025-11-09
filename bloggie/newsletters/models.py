from django.db import models
from django.core.validators import EmailValidator


class Newsletter(models.Model):
    """
    Newsletter subscription model for managing email subscribers.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Subscriber email
    email = models.EmailField(
        max_length=254,
        unique=True,
        validators=[EmailValidator()],
        help_text="Email address of the subscriber"
    )
    
    # Subscription timestamp
    subscribedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-subscribedAt']
        verbose_name = 'Newsletter Subscription'
        verbose_name_plural = 'Newsletter Subscriptions'
        indexes = [
            models.Index(fields=['-subscribedAt']),
            models.Index(fields=['email']),
        ]
    
    def __str__(self):
        return f"Newsletter subscription: {self.email}"
    
    def save(self, *args, **kwargs):
        # Ensure email is not empty and is lowercase
        if not self.email or not self.email.strip():
            raise ValueError("Email cannot be empty")
        self.email = self.email.lower().strip()
        super().save(*args, **kwargs)
