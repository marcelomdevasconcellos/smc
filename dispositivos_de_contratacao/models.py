# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class Licitacoes(BaseModel):
    cols = {
        'nome_orgao_ata': 6, 
        'cpf_gestor': 6, 
        'numero_licitacao': 6, 
        'tipo_licitacao': 6, 
        'modalidade_licitacao': 6, 
        'modalidade_processo_administrativo': 6, 
        'descricao1_motivo_fornecedor': 6, 
        'descricao2_motivo_fornecedor': 6, 
        'descricao1_objeto_licitacao': 6, 
        'descricao2_objeto_licitacao': 6, 
        'descricao1_justificativa_preco': 6, 
        'descricao2_justificativa_preco': 6, 
        'nome_responsavel_juridico': 6, 
        'cpf_responsavel_juridico': 6, 
        'nome_responsavel_homologacao': 6, 
        'cpf_responsavel_homologacao': 6, 
        'numero_comissao': 6, 
        'data_criacao_comissao': 6, 
        'data_emissao_edital': 6, 
        'data_homologacao': 6, 
        'data_realizacao_autuacao_licitacao': 6, 
        'data_realizacao_licitacao': 6, 
        'hora_licitacao': 6, 
        'valor_limite_superior': 6, 
        'valor_orcado_estimado': 6, }
    
    nome_orgao_ata = models.CharField(
        'Nome do Órgão', 
        max_length=200, )
    cpf_gestor = models.CharField(
        'CPF do Gestor', 
        max_length=11, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        choices=CHOICES_NUMERO_LICITACAO, 
        max_length=20, )
    tipo_licitacao = models.IntegerField(
        'Tipo de Licitação', )
    modalidade_licitacao = models.CharField(
        'Modalidade da Licitação', 
        max_length=20, )
    modalidade_processo_administrativo = models.CharField(
        'Modalidade do Processo Administrativo', 
        max_length=20, )
    descricao1_motivo_fornecedor = models.TextField(
        'Descrição do Motivo do Fornecedor', )
    descricao2_motivo_fornecedor = models.TextField(
        'Descrição do Motivo do Fornecedor', )
    descricao1_objeto_licitacao = models.TextField(
        'Descrição do Objeto da Licitação', )
    descricao2_objeto_licitacao = models.TextField(
        'Descrição do Objeto da Licitação', )
    descricao1_justificativa_preco = models.TextField(
        'Descrição/Justificativa de Preço', )
    descricao2_justificativa_preco = models.TextField(
        'Descrição/Justificativa de Preço', )
    nome_responsavel_juridico = models.CharField(
        'Nome do Responsável Jurídico', 
        max_length=200, )
    cpf_responsavel_juridico = models.CharField(
        'CPF do Responsável Jurídico', 
        max_length=11, )
    nome_responsavel_homologacao = models.CharField(
        'Nome do Responsável pela Homologação', 
        max_length=200, )
    cpf_responsavel_homologacao = models.CharField(
        'CPF do Responsável pela Homologação', 
        max_length=11, )
    numero_comissao = models.CharField(
        'Número da Comissão', 
        max_length=20, )
    data_criacao_comissao = models.DateField(
        'Data de Criação da Comissão', )
    data_emissao_edital = models.DateField(
        'Data de Emissão do Edital', )
    data_homologacao = models.DateField(
        'Data de Homologação', )
    data_realizacao_autuacao_licitacao = models.DateField(
        'Data de Realização da Autuação da Licitação', )
    data_realizacao_licitacao = models.DateField(
        'Data de Realização da Licitação', )
    hora_licitacao = models.CharField(
        'Hora de Realização da Licitação', 
        max_length=20, )
    valor_limite_superior = models.DecimalField(
        'Valor do Limite Superior',  
        max_digits=15, 
        decimal_places=2, )
    valor_orcado_estimado = models.DecimalField(
        'Valor Orçado Estimado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.nome_orgao_ata, self.cpf_gestor, self.numero_licitacao, self.tipo_licitacao, self.modalidade_licitacao, self.modalidade_processo_administrativo, self.descricao1_motivo_fornecedor, self.descricao2_motivo_fornecedor, self.descricao1_objeto_licitacao, self.descricao2_objeto_licitacao, self.descricao1_justificativa_preco, self.descricao2_justificativa_preco, self.nome_responsavel_juridico, self.cpf_responsavel_juridico, self.nome_responsavel_homologacao, self.cpf_responsavel_homologacao, self.numero_comissao, self.data_criacao_comissao, self.data_emissao_edital, self.data_homologacao, self.data_realizacao_autuacao_licitacao, self.data_realizacao_licitacao, self.hora_licitacao, self.valor_limite_superior, self.valor_orcado_estimado)

    class Meta:
        verbose_name = 'Licitação'
        verbose_name_plural = 'Licitações'



class LicitacoesDotacoes(BaseModel):
    cols = {
        'licitacao': 6, 
        'orcamento_despesa': 6, }
    
    licitacao = models.ForeignKey(
        'dispositivos_de_contratacao.Licitacoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_licitacao', )
    orcamento_despesa = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_despesa', )
    
    def __str__(self):
        return '{} - {}'.format(self.licitacao, self.orcamento_despesa)

    class Meta:
        verbose_name = 'Dotação da Licitação'
        verbose_name_plural = 'Dotações da Licitação'



class Dispensas(BaseModel):
    cols = {
        'credor': 6, 
        'numero': 6, 
        'dispositivo_legal': 6, 
        'num_processo': 6, 
        'descricao': 6, 
        'valor': 6, 
        'arquivo': 6, 
        'data_publicacao': 6, 
        'num_pagina_diario_oficial': 6, }
    
    credor = models.ForeignKey(
        'execucao_orcamentaria.Credores', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_credor', )
    numero = models.CharField(
        'Número da Dispensa', 
        max_length=10, )
    dispositivo_legal = models.ForeignKey(
        'cadastros_basicos.DispositivosLegais', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dispositivo_legal', )
    num_processo = models.CharField(
        'Número do Processo', 
        max_length=10, )
    descricao = models.TextField(
        'Descrição', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    data_publicacao = models.DateField(
        'Data de Publicação', )
    num_pagina_diario_oficial = models.DateField(
        'Número da Página no D.O.', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.credor, self.numero, self.dispositivo_legal, self.num_processo, self.descricao, self.valor, self.arquivo, self.data_publicacao, self.num_pagina_diario_oficial)

    class Meta:
        verbose_name = 'Dispensa'
        verbose_name_plural = 'Dispensas'



class DispensasDotacoes(BaseModel):
    cols = {
        'dispensa': 6, 
        'orcamento_despesa': 6, }
    
    dispensa = models.ForeignKey(
        'dispositivos_de_contratacao.Dispensas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dispensa', )
    orcamento_despesa = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_despesa', )
    
    def __str__(self):
        return '{} - {}'.format(self.dispensa, self.orcamento_despesa)

    class Meta:
        verbose_name = 'Dotação da Dispensa'
        verbose_name_plural = 'Dotações da Dispensa'



class Inexigibilidades(BaseModel):
    cols = {
        'credor': 6, 
        'numero': 6, 
        'dispositivo_legal': 6, 
        'num_processo': 6, 
        'descricao': 6, 
        'valor': 6, 
        'arquivo': 6, 
        'data_publicacao': 6, 
        'num_pagina_diario_oficial': 6, }
    
    credor = models.ForeignKey(
        'execucao_orcamentaria.Credores', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_credor', )
    numero = models.CharField(
        'Número da Dispensa', 
        max_length=10, )
    dispositivo_legal = models.ForeignKey(
        'cadastros_basicos.DispositivosLegais', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dispositivo_legal', )
    num_processo = models.CharField(
        'Número do Processo', 
        max_length=10, )
    descricao = models.TextField(
        'Descrição', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    data_publicacao = models.DateField(
        'Data de Publicação', )
    num_pagina_diario_oficial = models.DateField(
        'Número da Página no D.O.', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.credor, self.numero, self.dispositivo_legal, self.num_processo, self.descricao, self.valor, self.arquivo, self.data_publicacao, self.num_pagina_diario_oficial)

    class Meta:
        verbose_name = 'Inexigibilidade'
        verbose_name_plural = 'Inexigibilidades'



class InexigibilidadesDotacoes(BaseModel):
    cols = {
        'inexigibilidade': 6, 
        'orcamento_despesa': 6, }
    
    inexigibilidade = models.ForeignKey(
        'dispositivos_de_contratacao.Inexigibilidades', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_inexigibilidade', )
    orcamento_despesa = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_despesa', )
    
    def __str__(self):
        return '{} - {}'.format(self.inexigibilidade, self.orcamento_despesa)

    class Meta:
        verbose_name = 'Dotação da Inexigibilidade'
        verbose_name_plural = 'Dotações da Inexigibilidade'