# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    DespesasSemContrato,
    DespesasSemContratoArquivos,
    DespesasSemContratoCronogramaMensal,
    DespesasSemContratoDotacoes,
)



@admin.register(DespesasSemContrato)
class DespesasSemContratoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'conta_controle',
        'cod_orgao',
        'credor',
        'objeto',
        'justificativa',
        'fundamentacao',
        'num_documento',
        'tipo',
        'classificacao',
        'num_processo',
        'status',
        'tipo_objeto',
        'num_sic',
        'tipo_modalidade_aquisicao',
        'dispositivo_legal',
        'licitacao',
        'dispensa',
        'inexigibilidade',
        'valor_original',
        'valor_contrapartida',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_publicacao_portal',
        'data_inicio',
        'vigencia',
        'data_termino',
        'arquivo',
    )
    list_filter = (
        'conta_controle',
        'cod_orgao',
        'credor',
        'objeto',
        'justificativa',
        'fundamentacao',
        'num_documento',
        'tipo',
        'classificacao',
        'num_processo',
        'status',
        'tipo_objeto',
        'num_sic',
        'tipo_modalidade_aquisicao',
        'dispositivo_legal',
        'licitacao',
        'dispensa',
        'inexigibilidade',
        'valor_original',
        'valor_contrapartida',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_publicacao_portal',
        'data_inicio',
        'vigencia',
        'data_termino',
        'arquivo',
    )
    list_display = (
        'conta_controle',
        'cod_orgao',
        'credor',
        'objeto',
        'justificativa',
        'fundamentacao',
        'num_documento',
        'tipo',
        'classificacao',
        'num_processo',
        'status',
        'tipo_objeto',
        'num_sic',
        'tipo_modalidade_aquisicao',
        'dispositivo_legal',
        'licitacao',
        'dispensa',
        'inexigibilidade',
        'valor_original',
        'valor_contrapartida',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_publicacao_portal',
        'data_inicio',
        'vigencia',
        'data_termino',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasSemContratoArquivos)
class DespesasSemContratoArquivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesas_sem_contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_filter = (
        'despesas_sem_contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_display = (
        'despesas_sem_contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasSemContratoCronogramaMensal)
class DespesasSemContratoCronogramaMensalAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'ano',
        'despesas_sem_contrato',
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
        'ano',
        'despesas_sem_contrato',
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
        'ano',
        'despesas_sem_contrato',
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



@admin.register(DespesasSemContratoDotacoes)
class DespesasSemContratoDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'despesas_sem_contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_filter = (
        'despesas_sem_contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_display = (
        'despesas_sem_contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]