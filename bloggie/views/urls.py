from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewViewSet

router = DefaultRouter()
router.register(r'', ViewViewSet, basename='view')

urlpatterns = [
    path('', include(router.urls)),
]
