"""
URL configuration for bloggie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root - Welcome to Bloggie API
    """
    return Response({
        'message': 'Welcome to Bloggie API',
        'version': '1.0',
        'endpoints': {
            'users': reverse('user-list', request=request, format=format),
            'posts': reverse('post-list', request=request, format=format),
            'comments': reverse('comment-list', request=request, format=format),
            'contacts': reverse('contact-list', request=request, format=format),
            'follows': reverse('follow-list', request=request, format=format),
            'likes': reverse('like-list', request=request, format=format),
            'newsletters': reverse('newsletter-list', request=request, format=format),
            'shares': reverse('share-list', request=request, format=format),
            'views': reverse('view-list', request=request, format=format),
            'admin': '/admin/',
            'api-auth': '/api-auth/',
        }
    })


urlpatterns = [
    # Root - redirect to API root
    path('', api_root, name='api-root'),
    
    # Admin
    path("admin/", admin.site.urls),
    
    # API endpoints
    path("api/users/", include('users.urls')),
    path("api/posts/", include('posts.urls')),
    path("api/comments/", include('comments.urls')),
    path("api/contacts/", include('contacts.urls')),
    path("api/follows/", include('follows.urls')),
    path("api/likes/", include('likes.urls')),
    path("api/newsletters/", include('newsletters.urls')),
    path("api/shares/", include('shares.urls')),
    path("api/views/", include('views.urls')),
    
    # DRF auth endpoints
    path('api-auth/', include('rest_framework.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


