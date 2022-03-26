# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    PlanoPluriAnual,
    Secretarias,
    Orgaos,
    UnidadesOrcamentarias,
    UnidadesGestoras,
    Funcoes,
    SubFuncoes,
    Programas,
    Acoes,
    AcoesTipos,
    CategoriasEconomicas,
    GruposNaturezasDespesa,
    ModalidadesAplicacao,
    ElementosDespesa,
    Fontes,
    Rubricas,
    Origens,
    Especies,
    Alineas,
    SubAlineas,
    Orcamentos,
    OrcamentosReceitas,
    OrcamentosDespesas,
)



@admin.register(PlanoPluriAnual)
class PlanoPluriAnualAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'num_lei',
        'ano_inicio',
        'ano_termino',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
    )
    list_filter = (
        'num_lei',
        'ano_inicio',
        'ano_termino',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
    )
    list_display = (
        'num_lei',
        'ano_inicio',
        'ano_termino',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Secretarias)
class SecretariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Orgaos)
class OrgaosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'secretaria',
        'codigo',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'secretaria',
        'codigo',
        'titulo',
    )
    list_display = (
        'orcamento',
        'secretaria',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(UnidadesOrcamentarias)
class UnidadesOrcamentariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'orgao',
        'codigo',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'orgao',
        'codigo',
        'titulo',
    )
    list_display = (
        'orcamento',
        'orgao',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(UnidadesGestoras)
class UnidadesGestorasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'cnpj',
        'codigo',
        'codigo_credor',
        'poder',
        'sigla',
        'tipo_administracao',
        'tipo_unidade_gestora',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'cnpj',
        'codigo',
        'codigo_credor',
        'poder',
        'sigla',
        'tipo_administracao',
        'tipo_unidade_gestora',
        'titulo',
    )
    list_display = (
        'orcamento',
        'cnpj',
        'codigo',
        'codigo_credor',
        'poder',
        'sigla',
        'tipo_administracao',
        'tipo_unidade_gestora',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Funcoes)
class FuncoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'titulo',
    )
    list_filter = (
        'codigo',
        'titulo',
    )
    list_display = (
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(SubFuncoes)
class SubFuncoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'funcao',
        'codigo',
        'titulo',
    )
    list_filter = (
        'funcao',
        'codigo',
        'titulo',
    )
    list_display = (
        'funcao',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Programas)
class ProgramasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'planoplurianual',
        'codigo',
        'titulo',
    )
    list_filter = (
        'planoplurianual',
        'codigo',
        'titulo',
    )
    list_display = (
        'planoplurianual',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Acoes)
class AcoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'funcao',
        'sub_funcao',
        'programa',
        'codigo',
        'titulo',
        'tipo',
        'valor_fixado',
    )
    list_filter = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'funcao',
        'sub_funcao',
        'programa',
        'codigo',
        'titulo',
        'tipo',
        'valor_fixado',
    )
    list_display = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'funcao',
        'sub_funcao',
        'programa',
        'codigo',
        'titulo',
        'tipo',
        'valor_fixado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AcoesTipos)
class AcoesTiposAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'titulo',
    )
    list_filter = (
        'codigo',
        'titulo',
    )
    list_display = (
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(CategoriasEconomicas)
class CategoriasEconomicasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(GruposNaturezasDespesa)
class GruposNaturezasDespesaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ModalidadesAplicacao)
class ModalidadesAplicacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ElementosDespesa)
class ElementosDespesaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Fontes)
class FontesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Rubricas)
class RubricasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Origens)
class OrigensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Especies)
class EspeciesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Alineas)
class AlineasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(SubAlineas)
class SubAlineasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Orcamentos)
class OrcamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'planoplurianual',
        'num_lei',
        'ano_exercicio',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
        'percentual_suplementacao',
        'valor_total_fixado_orcamento',
        'valor_total_suplementacao_orcamento',
    )
    list_filter = (
        'planoplurianual',
        'num_lei',
        'ano_exercicio',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
        'percentual_suplementacao',
        'valor_total_fixado_orcamento',
        'valor_total_suplementacao_orcamento',
    )
    list_display = (
        'planoplurianual',
        'num_lei',
        'ano_exercicio',
        'data_aprovacao',
        'data_envio',
        'data_publicacao',
        'percentual_suplementacao',
        'valor_total_fixado_orcamento',
        'valor_total_suplementacao_orcamento',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosReceitas)
class OrcamentosReceitasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'fonte',
        'rubrica',
        'valor_previsto',
    )
    list_filter = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'fonte',
        'rubrica',
        'valor_previsto',
    )
    list_display = (
        'orcamento',
        'orgao',
        'unidade_orcamentaria',
        'fonte',
        'rubrica',
        'valor_previsto',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosDespesas)
class OrcamentosDespesasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'funcao',
        'acao',
        'elemento_despesa',
        'codigo_reduzido',
        'valor_dotacao_fixado',
    )
    list_filter = (
        'funcao',
        'acao',
        'elemento_despesa',
        'codigo_reduzido',
        'valor_dotacao_fixado',
    )
    list_display = (
        'funcao',
        'acao',
        'elemento_despesa',
        'codigo_reduzido',
        'valor_dotacao_fixado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]