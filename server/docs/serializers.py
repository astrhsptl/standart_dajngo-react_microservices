from rest_framework import serializers

from .models import (
    LoadedFiles, CodedFiles,
)

class LoadedFilesSerializer(serializers.ModelSerializer):
    '''Serializer for loaded files. Catching title, discription, file, published, loaded date'''
    class Meta:
        model = LoadedFiles
        fields = '__all__'

class CodedFilesSerializer(serializers.ModelSerializer):
    '''Serializer for loaded files. Catching title, discription, file, published, algorithm, coded date'''
    class Meta:
        model = CodedFiles
        fields = '__all__'
