from django.urls import path

from .views import (
    # Code alghorythms
    CodeAlghorythmAPIView, CodeAlghorythmRetrieveAPIView,

    # Loaded files
    LoadedFilesAPIView, LoadedFilesRetrieveAPIView,

    # Coded files
    CodedFilesAPIView, CodedFilesRetrieveAPIView,
)


urlpatterns = [
    # Code alghorythms
    path('codealghorythms/', CodeAlghorythmAPIView.as_view(), name='code_alghorythms_list'),
    path('codealghorythms/<int:pk>/', CodeAlghorythmRetrieveAPIView.as_view(), name='code_alghorythms_retriave'),

    # Loaded files
    path('files/loaded/', LoadedFilesAPIView.as_view(), name='loaded_files_list'),
    path('files/loaded/<int:pk>/', LoadedFilesRetrieveAPIView.as_view(), name='loaded_files_detail'),

    # Coded files
    path('files/coded/', CodedFilesAPIView.as_view(), name='coded_files_list'),
    path('files/coded/<int:pk>/', CodedFilesRetrieveAPIView.as_view(), name='coded_files_detail'),

]
