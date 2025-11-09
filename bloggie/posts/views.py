from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer, PostListSerializer, PostCreateUpdateSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing blog posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'published', 'user', 'author']
    search_fields = ['title', 'content', 'excerpt', 'category']
    ordering_fields = ['createdAt', 'updatedAt', 'title', 'readingTime']
    ordering = ['-createdAt']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return PostCreateUpdateSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        queryset = Post.objects.all()
        
        # Filter by tags if provided
        tags = self.request.query_params.get('tags', None)
        if tags:
            tag_list = tags.split(',')
            queryset = queryset.filter(tags__overlap=tag_list)
        
        return queryset
    
    @action(detail=True, methods=['get'])
    def comments(self, request, slug=None):
        """Get all comments for a post"""
        post = self.get_object()
        comments = post.comments.all()
        from comments.serializers import CommentListSerializer
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def likes(self, request, slug=None):
        """Get all likes for a post"""
        post = self.get_object()
        likes = post.likes.all()
        from likes.serializers import LikeListSerializer
        serializer = LikeListSerializer(likes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def shares(self, request, slug=None):
        """Get all shares for a post"""
        post = self.get_object()
        shares = post.shares.all()
        from shares.serializers import ShareListSerializer
        serializer = ShareListSerializer(shares, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def views_count(self, request, slug=None):
        """Get view count for a post"""
        post = self.get_object()
        count = post.views.count()
        return Response({'views': count})
    
    @action(detail=True, methods=['post'])
    def publish(self, request, slug=None):
        """Publish a post"""
        post = self.get_object()
        post.published = True
        post.status = 'published'
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def unpublish(self, request, slug=None):
        """Unpublish a post"""
        post = self.get_object()
        post.published = False
        post.status = 'draft'
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

