from rest_framework import serializers
from .models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):
    """Serializer for the Newsletter model"""
    
    class Meta:
        model = Newsletter
        fields = ['id', 'email', 'subscribedAt']
        read_only_fields = ['id', 'subscribedAt']


class NewsletterSubscribeSerializer(serializers.ModelSerializer):
    """Serializer for newsletter subscriptions"""
    
    class Meta:
        model = Newsletter
        fields = ['email']
    
    def validate_email(self, value):
        # Check if email already exists
        if Newsletter.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already subscribed to the newsletter.")
        return value.lower()
