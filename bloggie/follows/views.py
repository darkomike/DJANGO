from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Follow
from .serializers import FollowSerializer, FollowCreateSerializer, FollowListSerializer

User = get_user_model()


class FollowViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing follow relationships.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['followerId', 'followingId']
    ordering = ['-createdAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return FollowCreateSerializer
        elif self.action == 'list':
            return FollowListSerializer
        return FollowSerializer
    
    @action(detail=False, methods=['post'])
    def follow_user(self, request):
        """Follow a user"""
        following_id = request.data.get('followingId')
        
        if not following_id:
            return Response(
                {'error': 'followingId is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            following_user = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if request.user.id == int(following_id):
            return Response(
                {'error': 'You cannot follow yourself'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if already following
        if Follow.objects.filter(followerId=request.user, followingId=following_user).exists():
            return Response(
                {'message': 'Already following this user'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        follow = Follow.objects.create(
            followerId=request.user,
            followingId=following_user
        )
        serializer = FollowSerializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def unfollow_user(self, request):
        """Unfollow a user"""
        following_id = request.data.get('followingId')
        
        if not following_id:
            return Response(
                {'error': 'followingId is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            follow = Follow.objects.get(
                followerId=request.user,
                followingId=following_id
            )
            follow.delete()
            return Response(
                {'message': 'Successfully unfollowed user'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Follow.DoesNotExist:
            return Response(
                {'error': 'Follow relationship not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def my_followers(self, request):
        """Get current user's followers"""
        follows = Follow.objects.filter(followingId=request.user)
        serializer = FollowListSerializer(follows, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_following(self, request):
        """Get users that current user follows"""
        follows = Follow.objects.filter(followerId=request.user)
        serializer = FollowListSerializer(follows, many=True)
        return Response(serializer.data)

