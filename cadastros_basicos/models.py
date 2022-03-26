# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class ArquivosTipos(BaseModel):
    cols = {
        'titulo': 6, 
        'referencia': 6, }
    
    titulo = models.CharField(
        'Título', 
        max_length=50, )
    referencia = models.IntegerField(
        'Referência', 
        choices=CHOICES_REFERENCIA, )
    
    def __str__(self):
        return '{} - {}'.format(self.titulo, self.referencia)

    class Meta:
        verbose_name = 'Tipo de Arquivo'
        verbose_name_plural = 'Tipos de Arquivos'



class DatasReferencia(BaseModel):
    cols = {
        'codigo': 6, 
        'mes': 6, 
        'ano': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=6, 
        blank=True, 
        null=True, )
    mes = models.IntegerField(
        'Mês', )
    ano = models.IntegerField(
        'Ano', )
    
    def __str__(self):
        return '{}'.format(self.ano)

    class Meta:
        verbose_name = 'Data de Referência'
        verbose_name_plural = 'Datas de Referência'



class DespesasTipo(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {}'.format(self.orcamento, self.codigo)

    class Meta:
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'



class DispositivosLegais(BaseModel):
    cols = {
        'tipo': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    tipo = models.IntegerField(
        'Tipo', 
        choices=CHOICES_TIPO, )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return ''.format()

    class Meta:
        verbose_name = 'Dispositivo Legal'
        verbose_name_plural = 'Dispositivos Legais (Licitação, Dispensa, Inexigibilidade)'



class Itens(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'



class Estados(BaseModel):
    cols = {
        'sigla': 6, 
        'nome': 6, }
    
    sigla = models.CharField(
        'Sigla', 
        max_length=2, )
    nome = models.CharField(
        'Nome', 
        max_length=50, )
    
    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'



class Municipios(BaseModel):
    cols = {
        'estado': 6, 
        'nome': 6, 
        'cidade_uf': 6, 
        'codigo_tcm': 6, 
        'codigo_ibge': 6, }
    
    estado = models.ForeignKey(
        'cadastros_basicos.Estados', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_estado', )
    nome = models.CharField(
        'Nome', 
        max_length=50, )
    cidade_uf = models.CharField(
        'Cidade (UF)', 
        max_length=55, )
    codigo_tcm = models.CharField(
        'Código TCM', 
        max_length=3, )
    codigo_ibge = models.CharField(
        'Código IBGE', 
        max_length=7, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.estado, self.nome, self.cidade_uf, self.codigo_tcm, self.codigo_ibge)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'



class RetencoesTipos(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.orcamento, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Tipo de Retenção'
        verbose_name_plural = 'Tipos de Retenções'



class Responsaveis(BaseModel):
    cols = {
        'nome': 6, 
        'cpf': 6, 
        'telefone': 6, 
        'email': 6, }
    
    nome = models.CharField(
        'Nome', 
        max_length=200, )
    cpf = models.CharField(
        'CPF', 
        max_length=14, )
    telefone = models.CharField(
        'Telefone', 
        max_length=100, )
    email = models.CharField(
        'E-mail', 
        max_length=100, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.nome, self.cpf, self.telefone, self.email)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'



class Setores(BaseModel):
    cols = {
        'nome': 6, 
        'sigla': 6, }
    
    nome = models.CharField(
        'Nome', 
        max_length=100, )
    sigla = models.CharField(
        'Sigla', 
        max_length=10, )
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.sigla)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'