from django.http import request
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.tokens import RefreshToken


def authentication(request: request, serializer_class: Serializer):
    '''Authenticate user by request, email and password. Return response detail with error/successful message and status code. If data is valid, authenticate user user'''
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    if not email:
        return {'detail': 'no email'}, status.HTTP_400_BAD_REQUEST

    if not password:
        return {'detail': 'no password'}, status.HTTP_400_BAD_REQUEST
    
    user = authenticate(request, email=email, password=password)

    if user:
        serializer = dict(serializer_class(user).data)
        tokens = _get_access_refresh_tokens_for_user(user)
        serializer['access'] = tokens['access'] 
        serializer['refresh'] = tokens['refresh']
        return serializer, status.HTTP_200_OK

    return {'detail': 'authentication error'}, status.HTTP_400_BAD_REQUEST

def register(request: request, serializer_class: Serializer):
    '''Register new user. Get request and serializer class. Retern new user params and access/refresh tokens'''
    data = serializer_class(data=request.data)
    if data.is_valid():
        user = data.save()
        tokens = _get_access_refresh_tokens_for_user(user)
        
        data = dict(data.data)
        data['access'] = tokens['access'] 
        data['refresh'] = tokens['refresh']

        return data, status.HTTP_200_OK

    return data.errors, status.HTTP_400_BAD_REQUEST

def _get_access_refresh_tokens_for_user(user) -> dict:
    '''Get django user object. Return access and refresh tokens'''
    if user is None:
        raise TypeError('This function get user but not None')
        
    tokens = RefreshToken.for_user(user)
    return {
        'refresh': str(tokens),
        'access': str(tokens.access_token),
    }
    