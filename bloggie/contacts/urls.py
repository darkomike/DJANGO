from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ContactCreateView

router = DefaultRouter()
router.register(r'', ContactViewSet, basename='contact')

urlpatterns = [
    path('submit/', ContactCreateView.as_view(), name='contact-submit'),
    path('', include(router.urls)),
]
