from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, 
    UserRegistrationView, 
    UserLoginView, 
    UserLogoutView,
    ForgotPasswordView,
    ResetPasswordView,
    ChangePasswordView
)

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', UserLogoutView.as_view(), name='logout'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('', include(router.urls)),
]
