import os
import textract

from rest_framework import status
from django.core.mail import send_mail

from server.settings import BASE_DIR, EMAIL_HOST_USER
from server.celery import app
from services.coding_alghorythms import (
    HaffmanAlghorythm, ChangingAlghorythm,
)
from docs.models import (
    LoadedFiles, CodedFiles
)

FILE_TYPES = ['txt', 'doc', 'docx', ]
ALGS = {
    'Changed alghorythm': ChangingAlghorythm,
    'Huffman alghorythm': HaffmanAlghorythm,
}

@app.task
def coding_and_create_new_coded_file(file: LoadedFiles, algorithm,):
    try:
        text = textract.process(os.path.join(os.path.join(BASE_DIR, 'media'), str(file.file)))
        coder = ALGS[algorithm](text)
        coder.encode()
        text = coder.coded_string

        coded = CodedFiles(
            title=file.title,
            discription=file.discription,
            author=file.author,
            published=file.published,
            text=text,
            algorithm=algorithm
        )
        
        coded.save()

        if file.author:
                send_mail(
                    'Finish encoding',
                    'We just finish encoding ur file',
                    EMAIL_HOST_USER,
                    [file.author.email],
                    fail_silently=False,
                )
    except:
        ...

def start_coding(request):
    request_json_data = dict(request.data)
    try:
        if 'file_id' in request_json_data.keys() and request_json_data['file_id'] is isinstance(request_json_data['file_id'], (int)) and request_json_data['alghorythm'] in ALGS.keys(): 
            file = LoadedFiles.objects.get(pk=request_json_data['file_id'])
            coding_and_create_new_coded_file.delay(file, request_json_data['alghorythm'])
            return {'Detail': 'Start coding'}, status.HTTP_200_OK
        return {'Detail': 'Bad argument'}, status.HTTP_400_BAD_REQUEST

    except:
        return {'Detail': 'Bad request'}, status.HTTP_400_BAD_REQUEST