from rest_framework import serializers

from .models import (
    CodeAlghorythm, LoadedFiles, CodedFiles,
)


class CodeAlghorythmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeAlghorythm
        fields = '__all__'

class LoadedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadedFiles
        fields = '__all__'

class CodedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodedFiles
        fields = '__all__'
