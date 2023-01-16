import uuid

from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class CodeAlghorythm(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     db_index=True,
    #     default=uuid.uuid4,
    #     editable=False,
    #     verbose_name='id',
    # )
    title = models.CharField(max_length=256)
    discription = models.CharField(max_length=4096)

    def get_absolute_url(self,):
        return reverse_lazy('code_alghorythms_retriave', kwargs={'pk': self.pk})

    # class Meta:
    #     db_table = 'algorithms'
    #     indexes = [
    #         models.Index(fields=['id'], name='id_index'),
    #     ]

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
    file = models.FileField(upload_to='uploads/loaded/%Y/%m/%d/')
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
    file = models.FileField(upload_to='uploads/coded/%Y/%m/%d/')
    algorithm = models.ForeignKey(CodeAlghorythm, models.CASCADE)
    coded_date = models.DateField(auto_now=True)

    def get_absolute_url(self,):
        return reverse_lazy('coded_files_detail', kwargs={'pk': self.pk})

    # class Meta:
    #     db_table = 'coded_files'
    #     indexes = [
    #         models.Index(fields=['id'], name='id_index',),
    #     ]