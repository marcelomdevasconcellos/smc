# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class Contratos(BaseModel):
    cols = {
        'unidade_orcamentaria': 6, 
        'credor': 6, 
        'objeto': 6, 
        'justificativa': 6, 
        'fundamentacao': 6, 
        'num_documento': 6, 
        'tipo': 6, 
        'classificacao': 6, 
        'num_processo': 6, 
        'status': 6, 
        'tipo_objeto': 6, 
        'num_sic': 6, 
        'tipo_modalidade_aquisicao': 6, 
        'dispositivo_legal': 6, 
        'licitacao': 6, 
        'dispensa': 6, 
        'inexigibilidade': 6, 
        'valor_original': 6, 
        'valor_contrapartida': 6, 
        'data_assinatura': 6, 
        'data_publicacao': 6, 
        'num_pagina_diario_oficial': 6, 
        'data_publicacao_portal': 6, 
        'data_inicio': 6, 
        'vigencia': 6, 
        'data_termino': 6, 
        'arquivo': 6, 
        'concluido_divida': 6, }
    
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
    credor = models.ForeignKey(
        'execucao_orcamentaria.Credores', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_credor', )
    objeto = models.TextField(
        'Objeto', )
    justificativa = models.TextField(
        'Justificativa', )
    fundamentacao = models.TextField(
        'Fundamentação', )
    num_documento = models.CharField(
        'Número do Documento', 
        max_length=50, )
    tipo = models.CharField(
        'Tipo', 
        max_length=50, )
    classificacao = models.CharField(
        'Classificação', 
        max_length=50, )
    num_processo = models.CharField(
        'Número do Processo', 
        max_length=50, )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
    tipo_objeto = models.IntegerField(
        'Tipo de Objeto', 
        choices=CHOICES_TIPO_OBJETO, )
    num_sic = models.CharField(
        'Número no Sistema Contratos', 
        max_length=50, )
    tipo_modalidade_aquisicao = models.IntegerField(
        'Tipo da Modalidade de Aquisição', 
        choices=CHOICES_TIPO_MODALIDADE_AQUISICAO, )
    dispositivo_legal = models.ForeignKey(
        'cadastros_basicos.DispositivosLegais', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dispositivo_legal', )
    licitacao = models.ForeignKey(
        'dispositivos_de_contratacao.Licitacoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_licitacao', )
    dispensa = models.ForeignKey(
        'dispositivos_de_contratacao.Dispensas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dispensa', )
    inexigibilidade = models.ForeignKey(
        'dispositivos_de_contratacao.Inexigibilidades', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_inexigibilidade', )
    valor_original = models.DecimalField(
        'Valor Original',  
        max_digits=15, 
        decimal_places=2, )
    valor_contrapartida = models.DecimalField(
        'Valor da Contra-Partida',  
        max_digits=15, 
        decimal_places=2, )
    data_assinatura = models.DateTimeField(
        'Data de Assinatura', 
        
        )
    data_publicacao = models.DateTimeField(
        'Data de Publicação', 
        
        )
    num_pagina_diario_oficial = models.IntegerField(
        'Página do Diário Oficial', )
    data_publicacao_portal = models.DateTimeField(
        'Data de Publicação no Portal', 
        
        )
    data_inicio = models.DateTimeField(
        'Data de Início', 
        
        )
    vigencia = models.IntegerField(
        'Vigência', )
    data_termino = models.DateTimeField(
        'Data de Término', 
        
        )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    concluido_divida = models.BooleanField(
        'Concluído com dívida?', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.unidade_orcamentaria, self.credor, self.objeto, self.justificativa, self.fundamentacao, self.num_documento, self.tipo, self.classificacao, self.num_processo, self.status, self.tipo_objeto, self.num_sic, self.tipo_modalidade_aquisicao, self.dispositivo_legal, self.licitacao, self.dispensa, self.inexigibilidade, self.valor_original, self.valor_contrapartida, self.data_assinatura, self.data_publicacao, self.num_pagina_diario_oficial, self.data_publicacao_portal, self.data_inicio, self.vigencia, self.data_termino, self.arquivo, self.concluido_divida)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'



class ContratosAditivos(BaseModel):
    cols = {
        'contrato': 6, 
        'data_assinatura': 6, 
        'data_publicacao': 6, 
        'num_pagina_diario_oficial': 6, 
        'data_inicio': 6, 
        'vigencia': 6, 
        'data_termino': 6, 
        'num_documento': 6, 
        'objeto': 6, 
        'tipo': 6, 
        'valor': 6, 
        'valor_contrapartida': 6, 
        'arquivo': 6, }
    
    contrato = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato', )
    data_assinatura = models.DateTimeField(
        'Data de Assinatura', 
        
        )
    data_publicacao = models.DateTimeField(
        'Data de Publicação', 
        
        )
    num_pagina_diario_oficial = models.IntegerField(
        'Página do Diário Oficial', )
    data_inicio = models.DateTimeField(
        'Data de Início', 
        
        )
    vigencia = models.IntegerField(
        'Vigência', )
    data_termino = models.DateTimeField(
        'Data de Término', 
        
        )
    num_documento = models.CharField(
        'Número do Documento', 
        max_length=50, )
    objeto = models.CharField(
        'Objeto', 
        max_length=500, )
    tipo = models.CharField(
        'Tipo', 
        max_length=50, )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    valor_contrapartida = models.DecimalField(
        'Valor da Contra-Partida',  
        max_digits=15, 
        decimal_places=2, )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.contrato, self.data_assinatura, self.data_publicacao, self.num_pagina_diario_oficial, self.data_inicio, self.vigencia, self.data_termino, self.num_documento, self.objeto, self.tipo, self.valor, self.valor_contrapartida, self.arquivo)

    class Meta:
        verbose_name = 'Aditivo do Contrato'
        verbose_name_plural = 'Aditivos do Contrato'



class ContratosArquivos(BaseModel):
    cols = {
        'contrato': 6, 
        'nome_arquivo': 6, 
        'tipo': 6, 
        'descricao': 6, 
        'arquivo': 6, }
    
    contrato = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato', )
    nome_arquivo = models.CharField(
        'Nome do Arquivo', 
        max_length=500, )
    tipo = models.ForeignKey(
        'cadastros_basicos.ArquivosTipos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_tipo', )
    descricao = models.CharField(
        'Descrição', 
        max_length=500, )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.contrato, self.nome_arquivo, self.tipo, self.descricao, self.arquivo)

    class Meta:
        verbose_name = 'Arquivo do Contrato'
        verbose_name_plural = 'Arquivos do Contrato'



class ContratosClassificacao(BaseModel):
    cols = {
        'codigo': 6, 
        'titulo': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Classificação do Contrato'
        verbose_name_plural = 'Classificações do Contrato'



class ContratosContasControle(BaseModel):
    cols = {
        'contrato': 6, 
        'conta_controle': 6, }
    
    contrato = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato', )
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    
    def __str__(self):
        return '{} - {}'.format(self.contrato, self.conta_controle)

    class Meta:
        verbose_name = 'Conta de Controle do Contrato'
        verbose_name_plural = 'Contas de Controle do Contrato'



class ContratosCronogramaMensal(BaseModel):
    cols = {
        'contrato': 6, 
        'orcamento': 6, 
        'valor_jan': 6, 
        'valor_fev': 6, 
        'valor_mar': 6, 
        'valor_abr': 6, 
        'valor_mai': 6, 
        'valor_jun': 6, 
        'valor_jul': 6, 
        'valor_ago': 6, 
        'valor_set': 6, 
        'valor_out': 6, 
        'valor_nov': 6, 
        'valor_dez': 6, }
    
    contrato = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato', )
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    valor_jan = models.DecimalField(
        'Valor de Janeiro',  
        max_digits=15, 
        decimal_places=2, )
    valor_fev = models.DecimalField(
        'Valor de Fevereiro',  
        max_digits=15, 
        decimal_places=2, )
    valor_mar = models.DecimalField(
        'Valor de Março',  
        max_digits=15, 
        decimal_places=2, )
    valor_abr = models.DecimalField(
        'Valor de Abril',  
        max_digits=15, 
        decimal_places=2, )
    valor_mai = models.DecimalField(
        'Valor de Maio',  
        max_digits=15, 
        decimal_places=2, )
    valor_jun = models.DecimalField(
        'Valor de Junho',  
        max_digits=15, 
        decimal_places=2, )
    valor_jul = models.DecimalField(
        'Valor de Julho',  
        max_digits=15, 
        decimal_places=2, )
    valor_ago = models.DecimalField(
        'Valor de Agosto',  
        max_digits=15, 
        decimal_places=2, )
    valor_set = models.DecimalField(
        'Valor de Setembro',  
        max_digits=15, 
        decimal_places=2, )
    valor_out = models.DecimalField(
        'Valor de Outubro',  
        max_digits=15, 
        decimal_places=2, )
    valor_nov = models.DecimalField(
        'Valor de Novembro',  
        max_digits=15, 
        decimal_places=2, )
    valor_dez = models.DecimalField(
        'Valor de Dezembro',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.contrato, self.orcamento, self.valor_jan, self.valor_fev, self.valor_mar, self.valor_abr, self.valor_mai, self.valor_jun, self.valor_jul, self.valor_ago, self.valor_set, self.valor_out, self.valor_nov, self.valor_dez)

    class Meta:
        verbose_name = 'Cronograma Mensal do Contrato'
        verbose_name_plural = 'Cronogramas Mensais do Contrato'



class ContratosDotacoes(BaseModel):
    cols = {
        'contrato': 6, 
        'orcamento': 6, 
        'dotacao': 6, 
        'valor': 6, }
    
    contrato = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato', )
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    dotacao = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dotacao', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.contrato, self.orcamento, self.dotacao, self.valor)

    class Meta:
        verbose_name = 'Dotação do Contrato'
        verbose_name_plural = 'Dotações do Contrato'