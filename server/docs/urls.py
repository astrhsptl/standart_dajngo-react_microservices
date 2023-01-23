from django.urls import path

from .views import (
    # Loaded files
    LoadedFilesAPIView, LoadedFilesRetrieveAPIView,

    # Coded files
    CodedFilesAPIView, CodedFilesRetrieveAPIView,
)


urlpatterns = [
    # Loaded files
    path('loaded/', LoadedFilesAPIView.as_view(), name='loaded_files_list'),
    path('loaded/<int:pk>/', LoadedFilesRetrieveAPIView.as_view(), name='loaded_files_detail'),

    # Coded files
    path('coded/', CodedFilesAPIView.as_view(), name='coded_files_list'),
    path('coded/<int:pk>/', CodedFilesRetrieveAPIView.as_view(), name='coded_files_detail'),

]
