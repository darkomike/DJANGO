from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import View
from users.serializers import UserProfileSerializer

User = get_user_model()


class ViewSerializer(serializers.ModelSerializer):
    """Serializer for the View model"""
    userId = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='userId',
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    post_title = serializers.CharField(source='postId.title', read_only=True)
    
    class Meta:
        model = View
        fields = [
            'id', 'postId', 'userId', 'user_id', 'post_title',
            'isGuest', 'viewedAt', 'createdAt'
        ]
        read_only_fields = ['id', 'viewedAt', 'createdAt']


class ViewCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating views"""
    
    class Meta:
        model = View
        fields = ['postId', 'userId', 'isGuest']
        extra_kwargs = {
            'userId': {'required': False, 'allow_null': True},
            'isGuest': {'required': False}
        }


class ViewListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing views"""
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = View
        fields = ['id', 'user_name', 'isGuest', 'viewedAt']
        read_only_fields = fields
    
    def get_user_name(self, obj):
        if obj.userId and not obj.isGuest:
            return obj.userId.username
        return 'Guest'
