from rest_framework.generics import (
    RetrieveAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from .serializers import (
    CodeAlghorythmSerializer, LoadedFilesSerializer, CodedFilesSerializer,
)

from .models import (
    CodeAlghorythm, LoadedFiles, CodedFiles,
)

'''
    Code alghorythms API part
'''

class CodeAlghorythmAPIView(ListCreateAPIView):
    ''' API for code alghorythm. Support get, post. Queryset - all fields '''
    queryset = CodeAlghorythm.objects.all()
    serializer_class = CodeAlghorythmSerializer

class CodeAlghorythmRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    ''' API for code alghorythm. Support get, put, delete. Queryset - concrete object '''
    queryset = CodeAlghorythm.objects.all()
    serializer_class = CodeAlghorythmSerializer


'''
    Loaded files API part
'''

class LoadedFilesAPIView(ListCreateAPIView):
    ''' API for loaded files. Support get, post. Queryset - all fields '''
    queryset = LoadedFiles.objects.all()
    serializer_class = LoadedFilesSerializer

class LoadedFilesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    ''' API for loaded files. Support get, put, delete. Queryset - concrete object '''
    queryset = LoadedFiles.objects.all()
    serializer_class = LoadedFilesSerializer


'''
    Coded files API part
'''

class CodedFilesAPIView(ListCreateAPIView):
    ''' API for coded files. Support get, post. Queryset - all fields '''
    queryset = CodedFiles.objects.all()
    serializer_class = CodedFilesSerializer

class CodedFilesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    ''' API for coded files. Support get, put, delete. Queryset - concrete object '''
    queryset = CodedFiles.objects.all()
    serializer_class = CodedFilesSerializer