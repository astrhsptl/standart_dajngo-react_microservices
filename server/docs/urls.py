from django.urls import path

from .views import (
    # Loaded files
    LoadedFilesAPIView, LoadedFilesRetrieveAPIView,

    # Coded files
    CodedFilesAPIView, CodedFilesRetrieveAPIView,

    StartCodingAPIView
)


urlpatterns = [
    # Loaded files
    path('loaded/', LoadedFilesAPIView.as_view(), name='loaded_files_list'),
    path('loaded/<int:pk>/', LoadedFilesRetrieveAPIView.as_view(), name='loaded_files_detail'),

    # Coded files
    path('coded/', CodedFilesAPIView.as_view(), name='coded_files_list'),
    path('coded/<int:pk>/', CodedFilesRetrieveAPIView.as_view(), name='coded_files_detail'),

    path('start_coding/', StartCodingAPIView.as_view(), name='start_coding')

]

'''
{
    "name": "asdf",
    "surname": "asf",
    "email": "asf@sdf.sadf",
    "password": "sadfgqwg",
    "is_superuser": false,
    "is_staff": false
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1MTEwODIzLCJqdGkiOiJkMDgwZDdhZmQ3Y2Q0NWQxYmU3YWZkMTlmZGNiYzU2MyIsInVzZXJfaWQiOjF9.g2YbXJUjF3s8ujVHKuxUz_iV8SoYQaEAgAI9Gty0McU",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NTE5NjkyMywianRpIjoiN2EyNDhhNzM0ZDZmNDRjNzlmMDc1N2U5ZmY0NDhiZWUiLCJ1c2VyX2lkIjoxfQ.cB4nW1TfQXuNQRZ9NjYnGsLS7jSffIGdSn4jj2CdG-w"
}
'''