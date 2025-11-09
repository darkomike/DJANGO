from django.db import models
from django.core.validators import EmailValidator


class Contact(models.Model):
    """
    Contact form submission model for storing user inquiries.
    """
    # Primary identifier
    id = models.AutoField(primary_key=True)
    
    # Contact information
    name = models.CharField(max_length=200, help_text="Name of the person contacting")
    email = models.EmailField(
        max_length=254,
        validators=[EmailValidator()],
        help_text="Email address for response"
    )
    
    # Message content
    message = models.TextField(help_text="Contact message content")
    
    # Timestamp
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-createdAt']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        indexes = [
            models.Index(fields=['-createdAt']),
            models.Index(fields=['email']),
        ]
    
    def __str__(self):
        return f"Contact from {self.name} ({self.email})"
    
    def save(self, *args, **kwargs):
        # Ensure required fields are not empty
        if not self.name or not self.name.strip():
            raise ValueError("Name cannot be empty")
        if not self.email or not self.email.strip():
            raise ValueError("Email cannot be empty")
        if not self.message or not self.message.strip():
            raise ValueError("Message cannot be empty")
        super().save(*args, **kwargs)
