from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Newsletter
from .serializers import NewsletterSerializer, NewsletterSubscribeSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing newsletter subscriptions.
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['-subscribedAt']
    
    def get_serializer_class(self):
        if self.action in ['create', 'subscribe']:
            return NewsletterSubscribeSerializer
        return NewsletterSerializer
    
    @action(detail=False, methods=['post'])
    def subscribe(self, request):
        """Subscribe to newsletter"""
        serializer = NewsletterSubscribeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Successfully subscribed to newsletter!'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def unsubscribe(self, request):
        """Unsubscribe from newsletter"""
        email = request.data.get('email')
        
        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            subscription = Newsletter.objects.get(email=email.lower())
            subscription.delete()
            return Response(
                {'message': 'Successfully unsubscribed from newsletter'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Newsletter.DoesNotExist:
            return Response(
                {'error': 'Email not found in subscription list'},
                status=status.HTTP_404_NOT_FOUND
            )


class NewsletterSubscribeView(generics.CreateAPIView):
    """
    View for newsletter subscription
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSubscribeSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Successfully subscribed to newsletter!'},
            status=status.HTTP_201_CREATED
        )

