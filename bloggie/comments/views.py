from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer, CommentListSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['postId', 'user']
    ordering = ['-createdAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'list':
            return CommentListSerializer
        return CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        
        # Filter by post if provided
        post_id = self.request.query_params.get('post', None)
        if post_id:
            queryset = queryset.filter(postId=post_id)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def my_comments(self, request):
        """Get comments by current user"""
        comments = Comment.objects.filter(user=request.user)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

