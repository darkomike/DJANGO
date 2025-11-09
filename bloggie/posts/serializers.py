from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post
from users.serializers import UserProfileSerializer

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model"""
    author = UserProfileSerializer(read_only=True)
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', 
        queryset=User.objects.all(),
        write_only=True
    )
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'category',
            'tags', 'author', 'author_id', 'user', 'user_id', 'status',
            'published', 'coverImage', 'readingTime', 'createdAt', 'updatedAt'
        ]
        read_only_fields = ['id', 'slug', 'readingTime', 'createdAt', 'updatedAt']


class PostListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing posts"""
    author_name = serializers.CharField(source='author.username', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'category', 'tags',
            'author_name', 'user_name', 'status', 'published',
            'coverImage', 'readingTime', 'createdAt'
        ]
        read_only_fields = fields


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating posts"""
    
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'content', 'excerpt', 'category',
            'tags', 'author', 'user', 'status', 'published', 'coverImage'
        ]
        extra_kwargs = {
            'slug': {'required': False},
        }
