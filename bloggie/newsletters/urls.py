from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsletterViewSet, NewsletterSubscribeView

router = DefaultRouter()
router.register(r'', NewsletterViewSet, basename='newsletter')

urlpatterns = [
    path('subscribe/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('', include(router.urls)),
]
