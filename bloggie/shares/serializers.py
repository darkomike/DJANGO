from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Share
from users.serializers import UserProfileSerializer

User = get_user_model()


class ShareSerializer(serializers.ModelSerializer):
    """Serializer for the Share model"""
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
        model = Share
        fields = [
            'id', 'postId', 'user', 'user_id', 'user_info', 'post_title',
            'platform', 'isGuest', 'sharedAt', 'createdAt'
        ]
        read_only_fields = ['id', 'sharedAt', 'createdAt', 'user_info']


class ShareCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating shares"""
    
    class Meta:
        model = Share
        fields = ['postId', 'user', 'platform', 'isGuest']
        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
            'isGuest': {'required': False},
            'platform': {'required': False}
        }


class ShareListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing shares"""
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Share
        fields = ['id', 'user_name', 'platform', 'isGuest', 'sharedAt']
        read_only_fields = fields
    
    def get_user_name(self, obj):
        if obj.user and not obj.isGuest:
            return obj.user.username
        return 'Guest/Anonymous'
