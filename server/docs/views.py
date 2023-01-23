from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from .serializers import (
    LoadedFilesSerializer, CodedFilesSerializer,
)

from .models import (
    LoadedFiles, CodedFiles,
)

from .permissions import IsOwnerPermission


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


'''
{
    "name": "van",
    "surname": "qwfiuhw",
    "email": "asd@adfqw.as",
    "password": "21c49oirt8y12t4p9h",
    "is_superuser": false,
    "is_staff": false,
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MDcxNjU2LCJqdGkiOiI3NTBhYjYxODk2ZTE0ZDgwODlhZGY5Yjk1NmY5YTI3OCIsInVzZXJfaWQiOjF9.oXt0xoo5tGmDK4Ir5fE0BXgLNW6k3DiqJlImWTisfUc",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDE1Nzc1NiwianRpIjoiZWNmM2ExYjEzZDExNDlhMGE5YjM4ZjYwNjdhODk0OTkiLCJ1c2VyX2lkIjoxfQ.-W767Ft04faK8LGbDVXjRuO2XaHclD4VuEoiWWEZGZo"
}
'''