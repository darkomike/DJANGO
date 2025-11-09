from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import View
from .serializers import ViewSerializer, ViewCreateSerializer, ViewListSerializer


class ViewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing post views.
    """
    queryset = View.objects.all()
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['postId', 'userId', 'isGuest']
    ordering = ['-viewedAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ViewCreateSerializer
        elif self.action == 'list':
            return ViewListSerializer
        return ViewSerializer
    
    def perform_create(self, serializer):
        serializer.save(userId=self.request.user, isGuest=False)
    
    def get_queryset(self):
        queryset = View.objects.all()
        
        # Filter by post if provided
        post_id = self.request.query_params.get('post', None)
        if post_id:
            queryset = queryset.filter(postId=post_id)
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def record_view(self, request):
        """Record a view on a post"""
        post_id = request.data.get('postId')
        
        if not post_id:
            return Response(
                {'error': 'postId is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create view record
        view = View.objects.create(
            postId_id=post_id,
            userId=request.user,
            isGuest=False
        )
        
        serializer = ViewSerializer(view)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def my_views(self, request):
        """Get views by current user"""
        views = View.objects.filter(userId=request.user)
        serializer = self.get_serializer(views, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def post_views_count(self, request):
        """Get view count for a specific post"""
        post_id = request.query_params.get('post', None)
        
        if not post_id:
            return Response(
                {'error': 'post parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        count = View.objects.filter(postId=post_id).count()
        unique_users = View.objects.filter(
            postId=post_id,
            isGuest=False
        ).values('userId').distinct().count()
        guest_views = View.objects.filter(
            postId=post_id,
            isGuest=True
        ).count()
        
        return Response({
            'total_views': count,
            'unique_users': unique_users,
            'guest_views': guest_views
        })

