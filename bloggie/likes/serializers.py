from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Like
from users.serializers import UserProfileSerializer

User = get_user_model()


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model"""
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
        model = Like
        fields = [
            'id', 'postId', 'user', 'user_id', 'user_info', 'post_title',
            'isGuest', 'likedAt', 'createdAt'
        ]
        read_only_fields = ['id', 'likedAt', 'createdAt', 'user_info']


class LikeCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating likes"""
    
    class Meta:
        model = Like
        fields = ['postId', 'user', 'isGuest']
        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
            'isGuest': {'required': False}
        }


class LikeListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing likes"""
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Like
        fields = ['id', 'user_name', 'isGuest', 'likedAt']
        read_only_fields = fields
    
    def get_user_name(self, obj):
        if obj.user and not obj.isGuest:
            return obj.user.username
        return 'Guest/Anonymous'
