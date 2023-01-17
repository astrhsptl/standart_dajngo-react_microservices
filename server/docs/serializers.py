from rest_framework import serializers

from .models import (
    CodeAlghorythm, LoadedFiles, CodedFiles,
)


class CodeAlghorythmSerializer(serializers.ModelSerializer):
    '''Serializer for code algorytms. Catching title and discription'''
    class Meta:
        model = CodeAlghorythm
        fields = '__all__'

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
