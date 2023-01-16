from django.http import request
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.serializers import Serializer


def authentication(request: request, serializer_class: Serializer):
    '''Authenticate user by request, email and password. Return response detail with error/successful message and status code. If data is valid, authenticate user user'''
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    if not email:
        return {'error': 'no email'}, status.HTTP_400_BAD_REQUEST

    if not password:
        return {'error': 'no password'}, status.HTTP_400_BAD_REQUEST
    
    user = authenticate(request, email=email, password=password)

    if user:
        serializer = serializer_class(user)
        return serializer.data, status.HTTP_200_OK

    return {'error': 'authentication error'}, status.HTTP_400_BAD_REQUEST

def register(request: request, serializer_class: Serializer):
    data = serializer_class(data=request.data)
    if data.is_valid():
        data.save()
        return data.data, status.HTTP_200_OK

    return data.errors, status.HTTP_400_BAD_REQUEST
    