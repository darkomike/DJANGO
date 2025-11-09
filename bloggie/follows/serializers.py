from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Follow
from users.serializers import UserProfileSerializer

User = get_user_model()


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for the Follow model"""
    followerId = UserProfileSerializer(read_only=True)
    followingId = UserProfileSerializer(read_only=True)
    follower_id = serializers.PrimaryKeyRelatedField(
        source='followerId',
        queryset=User.objects.all(),
        write_only=True
    )
    following_id = serializers.PrimaryKeyRelatedField(
        source='followingId',
        queryset=User.objects.all(),
        write_only=True
    )
    follower_info = serializers.ReadOnlyField()
    following_info = serializers.ReadOnlyField()
    
    class Meta:
        model = Follow
        fields = [
            'id', 'followerId', 'follower_id', 'followingId', 'following_id',
            'followerName', 'followerPhotoURL', 'followingName', 'followingPhotoURL',
            'follower_info', 'following_info', 'createdAt'
        ]
        read_only_fields = ['id', 'createdAt', 'follower_info', 'following_info']


class FollowCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating follow relationships"""
    
    class Meta:
        model = Follow
        fields = ['followerId', 'followingId']
    
    def validate(self, attrs):
        if attrs['followerId'] == attrs['followingId']:
            raise serializers.ValidationError("A user cannot follow themselves.")
        return attrs


class FollowListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing follows"""
    follower_username = serializers.CharField(source='followerId.username', read_only=True)
    following_username = serializers.CharField(source='followingId.username', read_only=True)
    
    class Meta:
        model = Follow
        fields = [
            'id', 'follower_username', 'following_username',
            'followerName', 'followingName', 'createdAt'
        ]
        read_only_fields = fields
