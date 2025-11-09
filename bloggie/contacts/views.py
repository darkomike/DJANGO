from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Contact
from .serializers import ContactSerializer, ContactCreateSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing contact submissions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['-createdAt']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ContactCreateSerializer
        return ContactSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Thank you for contacting us. We will get back to you soon!'},
            status=status.HTTP_201_CREATED
        )


class ContactCreateView(generics.CreateAPIView):
    """
    View for creating contact submissions
    """
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Thank you for contacting us. We will get back to you soon!'},
            status=status.HTTP_201_CREATED
        )

