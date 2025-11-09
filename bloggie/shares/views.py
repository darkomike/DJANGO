from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Share
from .serializers import ShareSerializer, ShareCreateSerializer, ShareListSerializer


class ShareViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing shares.
    """
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['postId', 'user', 'platform', 'isGuest']
    ordering = ['-sharedAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ShareCreateSerializer
        elif self.action == 'list':
            return ShareListSerializer
        return ShareSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, isGuest=False)
    
    def get_queryset(self):
        queryset = Share.objects.all()
        
        # Filter by post if provided
        post_id = self.request.query_params.get('post', None)
        if post_id:
            queryset = queryset.filter(postId=post_id)
        
        # Filter by platform if provided
        platform = self.request.query_params.get('platform', None)
        if platform:
            queryset = queryset.filter(platform=platform)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def my_shares(self, request):
        """Get shares by current user"""
        shares = Share.objects.filter(user=request.user)
        serializer = self.get_serializer(shares, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def platform_stats(self, request):
        """Get share statistics by platform"""
        from django.db.models import Count
        
        stats = Share.objects.values('platform').annotate(
            count=Count('id')
        ).order_by('-count')
        
        return Response(stats)

