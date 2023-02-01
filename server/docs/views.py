from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from services.start_coding import start_coding
from .serializers import (
    LoadedFilesSerializer, CodedFilesSerializer,
)
from .permissions import IsOwnerPermission
from .models import (
    LoadedFiles, CodedFiles,
)


FILE_TYPES = ['txt', 'doc', 'docx', ]

class StartCodingAPIView(APIView):
    '''
        Wait:
        {
            'file_id': int,
            'alghorythm': str
        }
    '''

    permission_classes = (IsAuthenticated,)

    def post(self, request,):
        start_coding(request)

        return Response({'message': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)



'''
    Loaded files API part
'''

class LoadedFilesAPIView(ListCreateAPIView):
    ''' API for loaded files. Support get, post. Queryset - all fields '''
    queryset = LoadedFiles.objects.all()
    serializer_class = LoadedFilesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return  LoadedFiles.objects.filter(author=self.request.user)
    

class LoadedFilesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    ''' API for loaded files. Support get, put, delete. Queryset - concrete object '''
    queryset = LoadedFiles.objects.all()
    serializer_class = LoadedFilesSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)

'''
    Coded files API part
'''

class CodedFilesAPIView(ListCreateAPIView):
    ''' API for coded files. Support get, post. Queryset - all fields '''
    queryset = CodedFiles.objects.all()
    serializer_class = CodedFilesSerializer
    permission_classes = (IsAuthenticated,)


class CodedFilesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    ''' API for coded files. Support get, put, delete. Queryset - concrete object '''
    queryset = CodedFiles.objects.all()
    serializer_class = CodedFilesSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)