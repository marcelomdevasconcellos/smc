# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    ContasControle,
    ContasControleAcoes,
    ContasControleElementosDespesa,
    ContasControleLimites,
    Despesas,
    DespesasAcompanhamentos,
    DespesasArquivos,
    DespesasFontes,
    DespesasHistorico,
    PreEmpenhos,
    PrePagamentos,
)



@admin.register(ContasControle)
class ContasControleAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
        'controla_limite_mensal',
        'instrumento_despesa',
    )
    list_filter = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
        'controla_limite_mensal',
        'instrumento_despesa',
    )
    list_display = (
        'orcamento',
        'codigo',
        'titulo',
        'descricao',
        'controla_limite_mensal',
        'instrumento_despesa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContasControleAcoes)
class ContasControleAcoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'acao',
        'valor',
    )
    list_filter = (
        'conta_controle',
        'acao',
        'valor',
    )
    list_display = (
        'conta_controle',
        'acao',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContasControleElementosDespesa)
class ContasControleElementosDespesaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'codigo',
    )
    list_filter = (
        'conta_controle',
        'codigo',
    )
    list_display = (
        'conta_controle',
        'codigo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContasControleLimites)
class ContasControleLimitesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'status',
        'tipo',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
    )
    list_filter = (
        'conta_controle',
        'status',
        'tipo',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
    )
    list_display = (
        'conta_controle',
        'status',
        'tipo',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Despesas)
class DespesasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    list_filter = (
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    list_display = (
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasAcompanhamentos)
class DespesasAcompanhamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesa',
        'descricao',
    )
    list_filter = (
        'despesa',
        'descricao',
    )
    list_display = (
        'despesa',
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasArquivos)
class DespesasArquivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesa',
        'tipo_arquivo',
        'descricao',
        'arquivo',
    )
    list_filter = (
        'despesa',
        'tipo_arquivo',
        'descricao',
        'arquivo',
    )
    list_display = (
        'despesa',
        'tipo_arquivo',
        'descricao',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasFontes)
class DespesasFontesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesa',
        'orcamento',
        'fonte',
        'valor',
    )
    list_filter = (
        'despesa',
        'orcamento',
        'fonte',
        'valor',
    )
    list_display = (
        'despesa',
        'orcamento',
        'fonte',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasHistorico)
class DespesasHistoricoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesa',
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    list_filter = (
        'despesa',
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    list_display = (
        'despesa',
        'conta_controle',
        'codigo',
        'titulo',
        'descricao',
        'tipo',
        'valor_total',
        'prazo_de_execucao',
        'status',
        'valor_jan',
        'valor_fev',
        'valor_mar',
        'valor_abr',
        'valor_mai',
        'valor_jun',
        'valor_jul',
        'valor_ago',
        'valor_set',
        'valor_out',
        'valor_nov',
        'valor_dez',
        'data_aprovacao',
        'data_inicio',
        'data_fim',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(PreEmpenhos)
class PreEmpenhosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'despesa',
        'ano_exercicio',
        'orgao',
        'unidade_orcamentaria',
        'natureza',
        'num_ned_ordinaria',
        'num_processo',
        'credor',
        'tipo_instrumento_despesa',
        'contrato_despesa',
        'convenio_despesa',
        'despesa_sem_contrato',
        'tipo_instrumento_receita',
        'contrato_receita',
        'convenio_receita',
        'dotacao',
        'valor',
        'status',
    )
    list_filter = (
        'conta_controle',
        'despesa',
        'ano_exercicio',
        'orgao',
        'unidade_orcamentaria',
        'natureza',
        'num_ned_ordinaria',
        'num_processo',
        'credor',
        'tipo_instrumento_despesa',
        'contrato_despesa',
        'convenio_despesa',
        'despesa_sem_contrato',
        'tipo_instrumento_receita',
        'contrato_receita',
        'convenio_receita',
        'dotacao',
        'valor',
        'status',
    )
    list_display = (
        'conta_controle',
        'despesa',
        'ano_exercicio',
        'orgao',
        'unidade_orcamentaria',
        'natureza',
        'num_ned_ordinaria',
        'num_processo',
        'credor',
        'tipo_instrumento_despesa',
        'contrato_despesa',
        'convenio_despesa',
        'despesa_sem_contrato',
        'tipo_instrumento_receita',
        'contrato_receita',
        'convenio_receita',
        'dotacao',
        'valor',
        'status',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(PrePagamentos)
class PrePagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'pre_empenho',
        'valor',
        'status',
    )
    list_filter = (
        'pre_empenho',
        'valor',
        'status',
    )
    list_display = (
        'pre_empenho',
        'valor',
        'status',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]