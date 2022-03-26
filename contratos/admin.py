# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    Contratos,
    ContratosAditivos,
    ContratosArquivos,
    ContratosClassificacao,
    ContratosContasControle,
    ContratosCronogramaMensal,
    ContratosDotacoes,
)



@admin.register(Contratos)
class ContratosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'unidade_orcamentaria',
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
        'concluido_divida',
    )
    list_filter = (
        'unidade_orcamentaria',
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
        'concluido_divida',
    )
    list_display = (
        'unidade_orcamentaria',
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
        'concluido_divida',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContratosAditivos)
class ContratosAditivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'contrato',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_inicio',
        'vigencia',
        'data_termino',
        'num_documento',
        'objeto',
        'tipo',
        'valor',
        'valor_contrapartida',
        'arquivo',
    )
    list_filter = (
        'contrato',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_inicio',
        'vigencia',
        'data_termino',
        'num_documento',
        'objeto',
        'tipo',
        'valor',
        'valor_contrapartida',
        'arquivo',
    )
    list_display = (
        'contrato',
        'data_assinatura',
        'data_publicacao',
        'num_pagina_diario_oficial',
        'data_inicio',
        'vigencia',
        'data_termino',
        'num_documento',
        'objeto',
        'tipo',
        'valor',
        'valor_contrapartida',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContratosArquivos)
class ContratosArquivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_filter = (
        'contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_display = (
        'contrato',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContratosClassificacao)
class ContratosClassificacaoAdmin(AuditoriaAdmin):
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



@admin.register(ContratosContasControle)
class ContratosContasControleAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'contrato',
        'conta_controle',
    )
    list_filter = (
        'contrato',
        'conta_controle',
    )
    list_display = (
        'contrato',
        'conta_controle',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ContratosCronogramaMensal)
class ContratosCronogramaMensalAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'contrato',
        'orcamento',
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
        'contrato',
        'orcamento',
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
        'contrato',
        'orcamento',
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



@admin.register(ContratosDotacoes)
class ContratosDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_filter = (
        'contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_display = (
        'contrato',
        'orcamento',
        'dotacao',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]