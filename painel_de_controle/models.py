# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class DashboardsReceitasDespesas(BaseModel):
    cols = {
        'ano': 6, 
        'mes': 6, 
        'ano_mes': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'fonte': 6, 
        'valor_previsto': 6, 
        'valor_arrecadado_realizado': 6, 
        'valor_arrecadado_anulado': 6, 
        'valor_arrecadado': 6, 
        'valor_arrecadado_realizado_total': 6, 
        'valor_arrecadado_anulado_total': 6, 
        'valor_arrecadado_total': 6, 
        'valor_lei': 6, 
        'valor_dotacao_suplementacao': 6, 
        'valor_dotacao_anulacao': 6, 
        'valor_lei_credito': 6, 
        'valor_empenhado_realizado': 6, 
        'valor_empenhado_anulado': 6, 
        'valor_empenhado': 6, 
        'valor_liquidado_realizado': 6, 
        'valor_liquidado_estornado': 6, 
        'valor_liquidado': 6, 
        'valor_pago_realizado': 6, 
        'valor_pago_estornado': 6, 
        'valor_pago': 6, 
        'valor_saldo_dotacao': 6, 
        'valor_dotacao_suplementacao_total': 6, 
        'valor_dotacao_anulacao_total': 6, 
        'valor_lei_credito_total': 6, 
        'valor_empenhado_realizado_total': 6, 
        'valor_empenhado_anulado_total': 6, 
        'valor_empenhado_total': 6, 
        'valor_liquidado_realizado_total': 6, 
        'valor_liquidado_estornado_total': 6, 
        'valor_liquidado_total': 6, 
        'valor_pago_realizado_total': 6, 
        'valor_pago_estornado_total': 6, 
        'valor_pago_total': 6, }
    
    ano = models.IntegerField(
        'Ano', )
    mes = models.IntegerField(
        'Mês', 
        choices=CHOICES_MES, )
    ano_mes = models.IntegerField(
        'Ano-Mês', )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
    fonte = models.ForeignKey(
        'planejamento.Fontes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_fonte', )
    valor_previsto = models.DecimalField(
        'Valor Previsto',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_realizado = models.DecimalField(
        'Valor Realizado das Arrecadações',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_anulado = models.DecimalField(
        'Valor Anulado de Arrecadação',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado = models.DecimalField(
        'Valor Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_realizado_total = models.DecimalField(
        'Valor Total Realizado das Arrecadações',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_anulado_total = models.DecimalField(
        'Valor Total Anulado de Arrecadação',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_total = models.DecimalField(
        'Valor Total Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    valor_lei = models.DecimalField(
        'Valor Lei',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_suplementacao = models.DecimalField(
        'Valor Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulacao = models.DecimalField(
        'Valor Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_lei_credito = models.DecimalField(
        'Valor Lei+Crédito',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_realizado = models.DecimalField(
        'Valor Realizado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado = models.DecimalField(
        'Valor Anulado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado = models.DecimalField(
        'Valor Empenhado (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_realizado = models.DecimalField(
        'Valor Realizado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_estornado = models.DecimalField(
        'Valor Estornado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_realizado = models.DecimalField(
        'Valor Realizado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_estornado = models.DecimalField(
        'Valor Estornado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago = models.DecimalField(
        'Valor Pago (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_saldo_dotacao = models.DecimalField(
        'Valor Saldo Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_suplementacao_total = models.DecimalField(
        'Valor Total Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulacao_total = models.DecimalField(
        'Valor Total Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_lei_credito_total = models.DecimalField(
        'Valor Total Lei+Crédito Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_realizado_total = models.DecimalField(
        'Valor Total Realizado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado_total = models.DecimalField(
        'Valor Total Anulado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_total = models.DecimalField(
        'Valor Total Empenhado Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_realizado_total = models.DecimalField(
        'Valor Total Realizado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_estornado_total = models.DecimalField(
        'Valor Total Estornado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_total = models.DecimalField(
        'Valor Total Liquidado Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_realizado_total = models.DecimalField(
        'Valor Total Realizado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_estornado_total = models.DecimalField(
        'Valor Total Estornado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_total = models.DecimalField(
        'Valor Total Pago',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.ano, self.mes, self.ano_mes, self.orgao, self.unidade_orcamentaria, self.fonte, self.valor_previsto, self.valor_arrecadado_realizado, self.valor_arrecadado_anulado, self.valor_arrecadado, self.valor_arrecadado_realizado_total, self.valor_arrecadado_anulado_total, self.valor_arrecadado_total, self.valor_lei, self.valor_dotacao_suplementacao, self.valor_dotacao_anulacao, self.valor_lei_credito, self.valor_empenhado_realizado, self.valor_empenhado_anulado, self.valor_empenhado, self.valor_liquidado_realizado, self.valor_liquidado_estornado, self.valor_liquidado, self.valor_pago_realizado, self.valor_pago_estornado, self.valor_pago, self.valor_saldo_dotacao, self.valor_dotacao_suplementacao_total, self.valor_dotacao_anulacao_total, self.valor_lei_credito_total, self.valor_empenhado_realizado_total, self.valor_empenhado_anulado_total, self.valor_empenhado_total, self.valor_liquidado_realizado_total, self.valor_liquidado_estornado_total, self.valor_liquidado_total, self.valor_pago_realizado_total, self.valor_pago_estornado_total, self.valor_pago_total)

    class Meta:
        verbose_name = 'Receita/Despesa (Dashboard)'
        verbose_name_plural = 'Receitas/Despesas (Dashboards)'



class DashboardsReceitas(BaseModel):
    cols = {
        'ano': 6, 
        'mes': 6, 
        'ano_mes': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'fonte': 6, 
        'receita_categoria_economica': 6, 
        'receita_origem': 6, 
        'receita_especie': 6, 
        'receita_rubrica': 6, 
        'receita_alinea': 6, 
        'receita_sub_alinea': 6, 
        'valor_previsto': 6, 
        'valor_arrecadado_realizado': 6, 
        'valor_arrecadado_anulado': 6, 
        'valor_arrecadado': 6, 
        'valor_arrecadado_realizado_total': 6, 
        'valor_arrecadado_anulado_total': 6, 
        'valor_arrecadado_total': 6, }
    
    ano = models.IntegerField(
        'Ano', )
    mes = models.IntegerField(
        'Mês', 
        choices=CHOICES_MES, )
    ano_mes = models.IntegerField(
        'Ano-Mês', )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
    fonte = models.ForeignKey(
        'planejamento.Fontes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_fonte', )
    receita_categoria_economica = models.ForeignKey(
        'planejamento.CategoriasEconomicas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_categoria_economica', )
    receita_origem = models.ForeignKey(
        'planejamento.Origens', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_origem', )
    receita_especie = models.ForeignKey(
        'planejamento.Especies', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_especie', )
    receita_rubrica = models.ForeignKey(
        'planejamento.Rubricas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_rubrica', )
    receita_alinea = models.ForeignKey(
        'planejamento.Alineas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_alinea', )
    receita_sub_alinea = models.ForeignKey(
        'planejamento.SubAlineas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_receita_sub_alinea', )
    valor_previsto = models.DecimalField(
        'Valor Previsto',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_realizado = models.DecimalField(
        'Valor Realizado das Arrecadações',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_anulado = models.DecimalField(
        'Valor Anulado de Arrecadação',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado = models.DecimalField(
        'Valor Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_realizado_total = models.DecimalField(
        'Valor Total Realizado das Arrecadações',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_anulado_total = models.DecimalField(
        'Valor Total Anulado de Arrecadação',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadado_total = models.DecimalField(
        'Valor Total Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.ano, self.mes, self.ano_mes, self.orgao, self.unidade_orcamentaria, self.fonte, self.receita_categoria_economica, self.receita_origem, self.receita_especie, self.receita_rubrica, self.receita_alinea, self.receita_sub_alinea, self.valor_previsto, self.valor_arrecadado_realizado, self.valor_arrecadado_anulado, self.valor_arrecadado, self.valor_arrecadado_realizado_total, self.valor_arrecadado_anulado_total, self.valor_arrecadado_total)

    class Meta:
        verbose_name = 'Receita (Dashboard)'
        verbose_name_plural = 'Receitas (Dashboards)'



class DashboardsDespesas(BaseModel):
    cols = {
        'ano': 6, 
        'mes': 6, 
        'ano_mes': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'fonte': 6, 
        'funcao': 6, 
        'sub_funcao': 6, 
        'programa': 6, 
        'acao': 6, 
        'acao_tipo': 6, 
        'despesa_categoria_economica': 6, 
        'despesa_grupo_natureza': 6, 
        'despesa_modalidade_aplicacao': 6, 
        'despesa_elemento_despesa': 6, 
        'valor_lei': 6, 
        'valor_dotacao_suplementacao': 6, 
        'valor_dotacao_anulacao': 6, 
        'valor_lei_credito': 6, 
        'valor_empenhado_realizado': 6, 
        'valor_empenhado_anulado': 6, 
        'valor_empenhado': 6, 
        'valor_liquidado_realizado': 6, 
        'valor_liquidado_estornado': 6, 
        'valor_liquidado': 6, 
        'valor_pago_realizado': 6, 
        'valor_pago_estornado': 6, 
        'valor_pago': 6, 
        'valor_saldo_dotacao': 6, 
        'valor_dotacao_suplementacao_total': 6, 
        'valor_dotacao_anulacao_total': 6, 
        'valor_lei_credito_total': 6, 
        'valor_empenhado_realizado_total': 6, 
        'valor_empenhado_anulado_total': 6, 
        'valor_empenhado_total': 6, 
        'valor_liquidado_realizado_total': 6, 
        'valor_liquidado_estornado_total': 6, 
        'valor_liquidado_total': 6, 
        'valor_pago_realizado_total': 6, 
        'valor_pago_estornado_total': 6, 
        'valor_pago_total': 6, }
    
    ano = models.IntegerField(
        'Ano', )
    mes = models.IntegerField(
        'Mês', )
    ano_mes = models.IntegerField(
        'Ano-Mês', )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
    fonte = models.ForeignKey(
        'planejamento.Fontes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_fonte', )
    funcao = models.ForeignKey(
        'planejamento.Funcoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_funcao', )
    sub_funcao = models.ForeignKey(
        'planejamento.SubFuncoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_sub_funcao', )
    programa = models.ForeignKey(
        'planejamento.Programas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_programa', )
    acao = models.ForeignKey(
        'planejamento.Acoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_acao', )
    acao_tipo = models.ForeignKey(
        'planejamento.AcoesTipos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_acao_tipo', )
    despesa_categoria_economica = models.ForeignKey(
        'planejamento.CategoriasEconomicas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa_categoria_economica', )
    despesa_grupo_natureza = models.ForeignKey(
        'planejamento.GruposNaturezasDespesa', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa_grupo_natureza', )
    despesa_modalidade_aplicacao = models.ForeignKey(
        'planejamento.ModalidadesAplicacao', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa_modalidade_aplicacao', )
    despesa_elemento_despesa = models.ForeignKey(
        'planejamento.ElementosDespesa', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_despesa_elemento_despesa', )
    valor_lei = models.DecimalField(
        'Valor Lei',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_suplementacao = models.DecimalField(
        'Valor Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulacao = models.DecimalField(
        'Valor Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_lei_credito = models.DecimalField(
        'Valor Lei+Crédito',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_realizado = models.DecimalField(
        'Valor Realizado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado = models.DecimalField(
        'Valor Anulado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado = models.DecimalField(
        'Valor Empenhado (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_realizado = models.DecimalField(
        'Valor Realizado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_estornado = models.DecimalField(
        'Valor Estornado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_realizado = models.DecimalField(
        'Valor Realizado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_estornado = models.DecimalField(
        'Valor Estornado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago = models.DecimalField(
        'Valor Pago (Nominal)',  
        max_digits=15, 
        decimal_places=2, )
    valor_saldo_dotacao = models.DecimalField(
        'Valor Saldo Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_suplementacao_total = models.DecimalField(
        'Valor Total Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulacao_total = models.DecimalField(
        'Valor Total Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_lei_credito_total = models.DecimalField(
        'Valor Total Lei+Crédito Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_realizado_total = models.DecimalField(
        'Valor Total Realizado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado_total = models.DecimalField(
        'Valor Total Anulado de Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_total = models.DecimalField(
        'Valor Total Empenhado Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_realizado_total = models.DecimalField(
        'Valor Total Realizado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_estornado_total = models.DecimalField(
        'Valor Total Estornado de Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_total = models.DecimalField(
        'Valor Total Liquidado Total',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_realizado_total = models.DecimalField(
        'Valor Total Realizado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_estornado_total = models.DecimalField(
        'Valor Total Estornado de Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_total = models.DecimalField(
        'Valor Total Pago',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.ano, self.mes, self.ano_mes, self.orgao, self.unidade_orcamentaria, self.fonte, self.funcao, self.sub_funcao, self.programa, self.acao, self.acao_tipo, self.despesa_categoria_economica, self.despesa_grupo_natureza, self.despesa_modalidade_aplicacao, self.despesa_elemento_despesa, self.valor_lei, self.valor_dotacao_suplementacao, self.valor_dotacao_anulacao, self.valor_lei_credito, self.valor_empenhado_realizado, self.valor_empenhado_anulado, self.valor_empenhado, self.valor_liquidado_realizado, self.valor_liquidado_estornado, self.valor_liquidado, self.valor_pago_realizado, self.valor_pago_estornado, self.valor_pago, self.valor_saldo_dotacao, self.valor_dotacao_suplementacao_total, self.valor_dotacao_anulacao_total, self.valor_lei_credito_total, self.valor_empenhado_realizado_total, self.valor_empenhado_anulado_total, self.valor_empenhado_total, self.valor_liquidado_realizado_total, self.valor_liquidado_estornado_total, self.valor_liquidado_total, self.valor_pago_realizado_total, self.valor_pago_estornado_total, self.valor_pago_total)

    class Meta:
        verbose_name = 'Despesa (Dashboard)'
        verbose_name_plural = 'Despesas (Dashboards)'