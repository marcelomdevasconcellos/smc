# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class PlanoPluriAnual(BaseModel):
    cols = {
        'num_lei': 6, 
        'ano_inicio': 6, 
        'ano_termino': 6, 
        'data_aprovacao': 6, 
        'data_envio': 6, 
        'data_publicacao': 6, }
    
    num_lei = models.CharField(
        'Número da Lei', 
        max_length=20, )
    ano_inicio = models.CharField(
        'Ano de Início', 
        max_length=4, )
    ano_termino = models.CharField(
        'Ano de Término', 
        max_length=4, )
    data_aprovacao = models.DateField(
        'Data de Aprovação do PPA', )
    data_envio = models.DateField(
        'Data de Envio da PPA', )
    data_publicacao = models.DateField(
        'Data de Publicação da PPA', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.num_lei, self.ano_inicio, self.ano_termino, self.data_aprovacao, self.data_envio, self.data_publicacao)

    class Meta:
        verbose_name = 'PlanoPluriAnual'
        verbose_name_plural = 'PlanoPluriAnual'



class Secretarias(BaseModel):
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
        verbose_name = 'Secretaria'
        verbose_name_plural = 'Secretarias'



class Orgaos(BaseModel):
    cols = {
        'orcamento': 6, 
        'secretaria': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    secretaria = models.ForeignKey(
        'planejamento.Secretarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_secretaria', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.secretaria, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Órgão'
        verbose_name_plural = 'Órgãos'



class UnidadesOrcamentarias(BaseModel):
    cols = {
        'orcamento': 6, 
        'orgao': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.orgao, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Unidade Orçamentária'
        verbose_name_plural = 'Unidades Orçamentárias'



class UnidadesGestoras(BaseModel):
    cols = {
        'orcamento': 6, 
        'cnpj': 6, 
        'codigo': 6, 
        'codigo_credor': 6, 
        'poder': 6, 
        'sigla': 6, 
        'tipo_administracao': 6, 
        'tipo_unidade_gestora': 6, 
        'titulo': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    cnpj = models.CharField(
        'CNPJ', 
        max_length=50, )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    codigo_credor = models.CharField(
        'Código do Credor', 
        max_length=50, )
    poder = models.CharField(
        'Poder', 
        max_length=50, )
    sigla = models.CharField(
        'Sigla', 
        max_length=50, )
    tipo_administracao = models.CharField(
        'Tipo de Administração', 
        max_length=50, )
    tipo_unidade_gestora = models.IntegerField(
        'Tipo de Unidade Gestora', 
        choices=CHOICES_TIPO_UNIDADE_GESTORA, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.orcamento, self.cnpj, self.codigo, self.codigo_credor, self.poder, self.sigla, self.tipo_administracao, self.tipo_unidade_gestora, self.titulo)

    class Meta:
        verbose_name = 'Unidade Gestora'
        verbose_name_plural = 'Unidades Gestoras'



class Funcoes(BaseModel):
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
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'



class SubFuncoes(BaseModel):
    cols = {
        'funcao': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    funcao = models.ForeignKey(
        'planejamento.Funcoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_funcao', )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.funcao, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Sub-Função'
        verbose_name_plural = 'Sub-Funções'



class Programas(BaseModel):
    cols = {
        'planoplurianual': 6, 
        'codigo': 6, 
        'titulo': 6, }
    
    planoplurianual = models.ForeignKey(
        'planejamento.PlanoPluriAnual', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_planoplurianual', )
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.planoplurianual, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'



class Acoes(BaseModel):
    cols = {
        'orcamento': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'funcao': 6, 
        'sub_funcao': 6, 
        'programa': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'tipo': 6, 
        'valor_fixado': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    orgao = models.ForeignKey(
        'planejamento.Orgaos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orgao', )
    unidade_orcamentaria = models.ForeignKey(
        'planejamento.UnidadesOrcamentarias', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_unidade_orcamentaria', )
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
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=1000, )
    tipo = models.ForeignKey(
        'planejamento.AcoesTipos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_tipo', )
    valor_fixado = models.DecimalField(
        'Valor Fixado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.orcamento, self.orgao, self.unidade_orcamentaria, self.funcao, self.sub_funcao, self.programa, self.codigo, self.titulo, self.tipo, self.valor_fixado)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'



class AcoesTipos(BaseModel):
    cols = {
        'codigo': 6, 
        'titulo': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Tipo de Ação'
        verbose_name_plural = 'Tipos de Ações'



class CategoriasEconomicas(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
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
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Categoria Econômica'
        verbose_name_plural = 'Categorias Econômicas'



class GruposNaturezasDespesa(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
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
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Grupo de Natureza de Despesa'
        verbose_name_plural = 'Grupos de Naturezas de Despesa'



class ModalidadesAplicacao(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
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
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Modalidade de Aplicação'
        verbose_name_plural = 'Modalidades de Aplicação'



class ElementosDespesa(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
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
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Elemento de Despesa'
        verbose_name_plural = 'Elementos de Despesa'



class Fontes(BaseModel):
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
        verbose_name = 'Fonte'
        verbose_name_plural = 'Fontes'



class Rubricas(BaseModel):
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
        max_length=20, )
    titulo = models.TextField(
        'Titulo', )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.orcamento, self.codigo, self.titulo)

    class Meta:
        verbose_name = 'Rubrica'
        verbose_name_plural = 'Rubricas'



class Origens(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Origem'
        verbose_name_plural = 'Origens'



class Especies(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'



class Alineas(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Alínea'
        verbose_name_plural = 'Alíneas'



class SubAlineas(BaseModel):
    cols = {
        'orcamento': 6, 
        'codigo': 6, 
        'titulo': 6, 
        'descricao': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
    codigo = models.CharField(
        'Código', 
        max_length=10, )
    titulo = models.CharField(
        'Título', 
        max_length=200, )
    descricao = models.TextField(
        'Descrição', )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento, self.codigo, self.titulo, self.descricao)

    class Meta:
        verbose_name = 'Sub-Alínea'
        verbose_name_plural = 'Sub-Alíneas'



class Orcamentos(BaseModel):
    cols = {
        'planoplurianual': 6, 
        'num_lei': 6, 
        'ano_exercicio': 6, 
        'data_aprovacao': 6, 
        'data_envio': 6, 
        'data_publicacao': 6, 
        'percentual_suplementacao': 6, 
        'valor_total_fixado_orcamento': 6, 
        'valor_total_suplementacao_orcamento': 6, }
    
    planoplurianual = models.ForeignKey(
        'planejamento.PlanoPluriAnual', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_planoplurianual', )
    num_lei = models.CharField(
        'Número da Lei', 
        max_length=20, )
    ano_exercicio = models.IntegerField(
        'Ano de Exercício', )
    data_aprovacao = models.DateField(
        'Data de Aprovação da LOA', )
    data_envio = models.DateField(
        'Data de Envio da LOA', )
    data_publicacao = models.DateField(
        'Data de Publicação da LOA', )
    percentual_suplementacao = models.CharField(
        'Percentual de Suplementação do Orçamento', 
        max_length=20, )
    valor_total_fixado_orcamento = models.DecimalField(
        'Valor Total Fixado no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    valor_total_suplementacao_orcamento = models.DecimalField(
        'Valor Total de Suplementação no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.planoplurianual, self.num_lei, self.ano_exercicio, self.data_aprovacao, self.data_envio, self.data_publicacao, self.percentual_suplementacao, self.valor_total_fixado_orcamento, self.valor_total_suplementacao_orcamento)

    class Meta:
        verbose_name = 'Lei Orçamentária Anual'
        verbose_name_plural = 'Lei Orçamentária Anual'



class OrcamentosReceitas(BaseModel):
    cols = {
        'orcamento': 6, 
        'orgao': 6, 
        'unidade_orcamentaria': 6, 
        'fonte': 6, 
        'rubrica': 6, 
        'valor_previsto': 6, }
    
    orcamento = models.ForeignKey(
        'planejamento.Orcamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento', )
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
    rubrica = models.ForeignKey(
        'planejamento.Rubricas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_rubrica', )
    valor_previsto = models.DecimalField(
        'Valor Previsto',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.orcamento, self.orgao, self.unidade_orcamentaria, self.fonte, self.rubrica, self.valor_previsto)

    class Meta:
        verbose_name = 'Orçamento de Receitas'
        verbose_name_plural = 'Orçamento de Receitas'



class OrcamentosDespesas(BaseModel):
    cols = {
        'funcao': 6, 
        'acao': 6, 
        'elemento_despesa': 6, 
        'codigo_reduzido': 6, 
        'valor_dotacao_fixado': 6, }
    
    funcao = models.ForeignKey(
        'planejamento.Funcoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_funcao', )
    acao = models.ForeignKey(
        'planejamento.Acoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_acao', )
    elemento_despesa = models.ForeignKey(
        'planejamento.ElementosDespesa', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_elemento_despesa', )
    codigo_reduzido = models.CharField(
        'Código Reduzido', 
        max_length=50, )
    valor_dotacao_fixado = models.DecimalField(
        'Valor Fixado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.funcao, self.acao, self.elemento_despesa, self.codigo_reduzido, self.valor_dotacao_fixado)

    class Meta:
        verbose_name = 'Orçamento de Despesas'
        verbose_name_plural = 'Orçamento de Despesas'