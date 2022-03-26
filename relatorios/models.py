# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class Relatorios(BaseModel):
    cols = {
        'titulo': 6, 
        'campos': 6, 
        'sql': 6, }
    
    titulo = models.CharField(
        'Título', 
        max_length=30, )
    campos = models.TextField(
        'Lista dos Campos (separados por vírgula)', )
    sql = models.TextField(
        'SQL', )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.titulo, self.campos, self.sql)

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'