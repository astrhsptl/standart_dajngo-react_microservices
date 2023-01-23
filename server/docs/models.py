import uuid

from django.db import models
from django.urls import reverse_lazy

from authsystem.models import User

# Create your models here.


class LoadedFiles(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     db_index=True,
    #     default=uuid.uuid4,
    #     editable=False,
    #     verbose_name='id',
    # )
    title = models.CharField(max_length=256)
    discription = models.CharField(max_length=4096)
    # file = models.FileField(upload_to='uploads/loaded/%Y/%m/%d/')
    author = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    published = models.BooleanField(default=False)
    loaded_date = models.DateField(auto_now=True)

    def get_absolute_url(self,):
        return reverse_lazy('loaded_files_detail', kwargs={'pk': self.pk})

    # class Meta:
    #     db_table = 'loaded_files'
    #     indexes = [
    #         models.Index(fields=['id'], name='id_index'),
    #     ]

class CodedFiles(models.Model):
    ALGHORYTHMS = (
        (('alg1'), ('alg1')),
        (('alg2'), ('alg2')),
        (('alg3'), ('alg3')),
    )
    
    # id = models.UUIDField(
    #     primary_key=True,
    #     db_index=True,
    #     default=uuid.uuid4,
    #     editable=False,
    #     verbose_name='id',
    # )
    title = models.CharField(max_length=256)
    discription = models.CharField(max_length=4096)
    published = models.BooleanField(default=False)
    # file = models.FileField(upload_to='uploads/coded/%Y/%m/%d/')
    author = models.ForeignKey(User, models.CASCADE)
    algorithm = models.CharField(max_length=40, choices=ALGHORYTHMS)
    coded_date = models.DateField(auto_now=True)

    def get_absolute_url(self,):
        return reverse_lazy('coded_files_detail', kwargs={'pk': self.pk})

    # class Meta:
    #     db_table = 'coded_files'
    #     indexes = [
    #         models.Index(fields=['id'], name='id_index',),
    #     ]