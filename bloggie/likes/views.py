from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer, LikeCreateSerializer, LikeListSerializer


class LikeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing likes.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['postId', 'user', 'isGuest']
    ordering = ['-likedAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LikeCreateSerializer
        elif self.action == 'list':
            return LikeListSerializer
        return LikeSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, isGuest=False)
    
    def get_queryset(self):
        queryset = Like.objects.all()
        
        # Filter by post if provided
        post_id = self.request.query_params.get('post', None)
        if post_id:
            queryset = queryset.filter(postId=post_id)
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def toggle_like(self, request):
        """Toggle like on a post"""
        post_id = request.data.get('postId')
        
        if not post_id:
            return Response(
                {'error': 'postId is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check existing like
        existing_like = Like.objects.filter(
            postId=post_id,
            user=request.user
        ).first()
        
        if existing_like:
            existing_like.delete()
            return Response(
                {'message': 'Like removed', 'liked': False},
                status=status.HTTP_200_OK
            )
        else:
            like = Like.objects.create(
                postId_id=post_id,
                user=request.user,
                isGuest=False
            )
            serializer = LikeSerializer(like)
            return Response(
                {'message': 'Post liked', 'liked': True, 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
    
    @action(detail=False, methods=['get'])
    def my_likes(self, request):
        """Get likes by current user"""
        likes = Like.objects.filter(user=request.user)
        serializer = self.get_serializer(likes, many=True)
        return Response(serializer.data)

