from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comment
from users.serializers import UserProfileSerializer

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model"""
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    user_info = serializers.ReadOnlyField()
    post_title = serializers.CharField(source='postId.title', read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id', 'postId', 'user', 'user_id', 'user_info', 'post_title',
            'text', 'createdAt', 'updatedAt'
        ]
        read_only_fields = ['id', 'createdAt', 'updatedAt', 'user_info']


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating comments"""
    
    class Meta:
        model = Comment
        fields = ['postId', 'user', 'text']
        extra_kwargs = {
            'user': {'required': False, 'allow_null': True}
        }


class CommentListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing comments"""
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'text', 'createdAt']
        read_only_fields = fields
    
    def get_user_name(self, obj):
        return obj.user.username if obj.user else 'Anonymous'
