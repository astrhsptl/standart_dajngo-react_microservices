from rest_framework import serializers

from .models import User


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 
            'is_superuser', 'is_staff',
        )
        read_only_fields = ['token']

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=256
    )
    
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 
            'is_superuser', 'is_staff',
        )
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)