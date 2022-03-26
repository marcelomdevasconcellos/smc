# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class ContasControle(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, 
        'controla_limite_mensal': 6, 
        'instrumento_despesa': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=100, )
    descricao = models.CharField(
        'Descrição', 
        max_length=500, )
    controla_limite_mensal = models.IntegerField(
        'Controla Limite Mensal?', 
        choices=CHOICES_CONTROLA_LIMITE_MENSAL, )
    instrumento_despesa = models.IntegerField(
        'Executada por meio de Instrumento de Despesa?', 
        choices=CHOICES_INSTRUMENTO_DESPESA, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao, self.controla_limite_mensal, self.instrumento_despesa)

    class Meta:
        verbose_name = 'Conta de Controle'
        verbose_name_plural = 'Contas de Controle'



class ContasControleAcoes(BaseModel):
    cols = {
        'conta_controle': 6, 
        'acao': 6, 
        'valor': 6, }
    
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    acao = models.ForeignKey(
        'planejamento.Acoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_acao', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.conta_controle, self.acao, self.valor)

    class Meta:
        verbose_name = 'Ação vinculada a Conta de Controle'
        verbose_name_plural = 'Ações Vinculadas a Conta de Controle'



class ContasControleElementosDespesa(BaseModel):
    cols = {
        'conta_controle': 6, 
        'codigo': 6, }
    
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    codigo = models.ForeignKey(
        'planejamento.ElementosDespesa', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_codigo', )
    
    def __str__(self):
        return '{} - {}'.format(self.conta_controle, self.codigo)

    class Meta:
        verbose_name = 'Elemento de despesa vinculado a Conta de Controle'
        verbose_name_plural = 'Elementos de Despesa Vinculados a Conta de Controle'



class ContasControleLimites(BaseModel):
    cols = {
        'conta_controle': 6, 
        'status': 6, 
        'tipo': 6, 
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
    
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
    tipo = models.IntegerField(
        'Tipo', 
        choices=CHOICES_TIPO, )
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
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.conta_controle, self.status, self.tipo, self.valor_jan, self.valor_fev, self.valor_mar, self.valor_abr, self.valor_mai, self.valor_jun, self.valor_jul, self.valor_ago, self.valor_set, self.valor_out, self.valor_nov, self.valor_dez)

    class Meta:
        verbose_name = 'Limite da Conta de Controle'
        verbose_name_plural = 'Limites das Contas de Controle'



class Despesas(BaseModel):
    cols = {
        'conta_controle': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, 
        'tipo': 6, 
        'valor_total': 6, 
        'prazo_de_execucao': 6, 
        'status': 6, 
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
        'valor_dez': 6, 
        'data_aprovacao': 6, 
        'data_inicio': 6, 
        'data_fim': 6, }
    
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=100, )
    descricao = models.TextField(
        'Descrição', )
    tipo = models.IntegerField(
        'Tipo', 
        choices=CHOICES_TIPO, )
    valor_total = models.DecimalField(
        'Valor Total',  
        max_digits=15, 
        decimal_places=2, )
    prazo_de_execucao = models.IntegerField(
        'Prazo de Execução (em Meses)', )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
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
    data_aprovacao = models.DateTimeField(
        'Data de Aprovação', 
        
        )
    data_inicio = models.DateTimeField(
        'Data de Início', 
        
        )
    data_fim = models.DateTimeField(
        'Data de Término', 
        
        )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.conta_controle, self.codigo, self.titulo, self.descricao, self.tipo, self.valor_total, self.prazo_de_execucao, self.status, self.valor_jan, self.valor_fev, self.valor_mar, self.valor_abr, self.valor_mai, self.valor_jun, self.valor_jul, self.valor_ago, self.valor_set, self.valor_out, self.valor_nov, self.valor_dez, self.data_aprovacao, self.data_inicio, self.data_fim)

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'



class DespesasAcompanhamentos(BaseModel):
    cols = {
        'despesa': 6, 
        'descricao': 6, }
    
    despesa = models.ForeignKey(
        'controle.Despesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa', )
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {}'.format(self.despesa, self.descricao)

    class Meta:
        verbose_name = 'Acompanhamento da Despesa'
        verbose_name_plural = 'Acompanhamentos da Despesa'



class DespesasArquivos(BaseModel):
    cols = {
        'despesa': 6, 
        'tipo_arquivo': 6, 
        'descricao': 6, 
        'arquivo': 6, }
    
    despesa = models.ForeignKey(
        'controle.Despesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa', )
    tipo_arquivo = models.ForeignKey(
        'cadastros_basicos.ArquivosTipos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_tipo_arquivo', )
    descricao = models.CharField(
        'Descrição', 
        max_length=50, )
    arquivo = models.CharField(
        'Arquivo', 
        max_length=255, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.despesa, self.tipo_arquivo, self.descricao, self.arquivo)

    class Meta:
        verbose_name = 'Arquivo da Despesa'
        verbose_name_plural = 'Arquivos da Despesa'



class DespesasFontes(BaseModel):
    cols = {
        'despesa': 6, 
        'orcamento': 6, 
        'fonte': 6, 
        'valor': 6, }
    
    despesa = models.ForeignKey(
        'controle.Despesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa', )
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    fonte = models.ForeignKey(
        'planejamento.Fontes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_fonte', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.despesa, self.orcamento, self.fonte, self.valor)

    class Meta:
        verbose_name = 'Fonte da Despesa'
        verbose_name_plural = 'Fontes da Despesa'



class DespesasHistorico(BaseModel):
    cols = {
        'despesa': 6, 
        'conta_controle': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, 
        'tipo': 6, 
        'valor_total': 6, 
        'prazo_de_execucao': 6, 
        'status': 6, 
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
        'valor_dez': 6, 
        'data_aprovacao': 6, 
        'data_inicio': 6, 
        'data_fim': 6, }
    
    despesa = models.ForeignKey(
        'controle.Despesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa', )
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=100, )
    descricao = models.TextField(
        'Descrição', )
    tipo = models.IntegerField(
        'Tipo', 
        choices=CHOICES_TIPO, )
    valor_total = models.DecimalField(
        'Valor Total',  
        max_digits=15, 
        decimal_places=2, )
    prazo_de_execucao = models.IntegerField(
        'Prazo de Execução (em Meses)', )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
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
    data_aprovacao = models.DateTimeField(
        'Data de Aprovação', 
        
        )
    data_inicio = models.DateTimeField(
        'Data de Início', 
        
        )
    data_fim = models.DateTimeField(
        'Data de Término', 
        
        )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.despesa, self.conta_controle, self.codigo, self.titulo, self.descricao, self.tipo, self.valor_total, self.prazo_de_execucao, self.status, self.valor_jan, self.valor_fev, self.valor_mar, self.valor_abr, self.valor_mai, self.valor_jun, self.valor_jul, self.valor_ago, self.valor_set, self.valor_out, self.valor_nov, self.valor_dez, self.data_aprovacao, self.data_inicio, self.data_fim)

    class Meta:
        verbose_name = 'Histórico da Despesa'
        verbose_name_plural = 'Histórico da Despesa'



class PreEmpenhos(BaseModel):
    cols = {
        'conta_controle': 6, 
        'despesa': 6, 
        'ano_exercicio': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'natureza': 6, 
        'num_ned_ordinaria': 6, 
        'num_processo': 6, 
        'credor': 6, 
        'tipo_instrumento_despesa': 6, 
        'contrato_despesa': 6, 
        'convenio_despesa': 6, 
        'despesa_sem_contrato': 6, 
        'tipo_instrumento_receita': 6, 
        'contrato_receita': 6, 
        'convenio_receita': 6, 
        'dotacao': 6, 
        'valor': 6, 
        'status': 6, }
    
    conta_controle = models.ForeignKey(
        'controle.ContasControle', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_conta_controle', )
    despesa = models.ForeignKey(
        'controle.Despesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa', )
    ano_exercicio = models.CharField(
        'Ano de Exercício', 
        max_length=4, )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
    natureza = models.IntegerField(
        'Natureza', 
        choices=CHOICES_NATUREZA, )
    num_ned_ordinaria = models.CharField(
        'Número do Empenho Ordinário', 
        max_length=50, )
    num_processo = models.CharField(
        'Número do Processo', 
        max_length=20, )
    credor = models.ForeignKey(
        'execucao_orcamentaria.Credores', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_credor', )
    tipo_instrumento_despesa = models.IntegerField(
        'Tipo de Instrumento de Despesa', 
        choices=CHOICES_TIPO_INSTRUMENTO_DESPESA, )
    contrato_despesa = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato_despesa', )
    convenio_despesa = models.ForeignKey(
        'convenios.Convenios', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_convenio_despesa', )
    despesa_sem_contrato = models.ForeignKey(
        'despesas_sem_contrato.DespesasSemContrato', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa_sem_contrato', )
    tipo_instrumento_receita = models.IntegerField(
        'Tipo de Instrumento de Receita', 
        choices=CHOICES_TIPO_INSTRUMENTO_RECEITA, )
    contrato_receita = models.ForeignKey(
        'contratos.Contratos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_contrato_receita', )
    convenio_receita = models.ForeignKey(
        'convenios.Convenios', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_convenio_receita', )
    dotacao = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_dotacao', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.conta_controle, self.despesa, self.ano_exercicio, self.orgao, self.unidade_orcamentaria, self.natureza, self.num_ned_ordinaria, self.num_processo, self.credor, self.tipo_instrumento_despesa, self.contrato_despesa, self.convenio_despesa, self.despesa_sem_contrato, self.tipo_instrumento_receita, self.contrato_receita, self.convenio_receita, self.dotacao, self.valor, self.status)

    class Meta:
        verbose_name = 'Pré-Empenho'
        verbose_name_plural = 'Pré-Empenhos'



class PrePagamentos(BaseModel):
    cols = {
        'pre_empenho': 6, 
        'valor': 6, 
        'status': 6, }
    
    pre_empenho = models.ForeignKey(
        'controle.PreEmpenhos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_pre_empenho', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.pre_empenho, self.valor, self.status)

    class Meta:
        verbose_name = 'Pré-Pagamento'
        verbose_name_plural = 'Pré-Pagamentos'