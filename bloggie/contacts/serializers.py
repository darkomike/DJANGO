from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for the Contact model"""
    
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'createdAt']
        read_only_fields = ['id', 'createdAt']


class ContactCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating contact submissions"""
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
    
    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value
