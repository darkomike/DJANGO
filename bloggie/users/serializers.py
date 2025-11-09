from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""
    
    class Meta:
        model = User
        fields = [
            'id', 'uid', 'username', 'email', 'name', 'displayName',
            'avatar', 'photoURL', 'bio', 'github', 'linkedin', 'twitter',
            'website', 'role', 'status', 'createdAt', 'updatedAt',
            'first_name', 'last_name', 'is_active', 'is_staff'
        ]
        read_only_fields = ['id', 'uid', 'createdAt', 'updatedAt']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new users"""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password2', 'name',
            'displayName', 'bio', 'role', 'status'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile information"""
    
    class Meta:
        model = User
        fields = [
            'uid', 'username', 'name', 'displayName', 'email',
            'avatar', 'photoURL', 'bio', 'github', 'linkedin',
            'twitter', 'website', 'role', 'status', 'createdAt'
        ]
        read_only_fields = ['uid', 'username', 'createdAt']
