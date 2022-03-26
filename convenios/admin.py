# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    Convenios,
    ConveniosAditivos,
    ConveniosArquivos,
    ConveniosContasControle,
    ConveniosCronogramaMensal,
    ConveniosDotacoes,
)



@admin.register(Convenios)
class ConveniosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
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
        'concluido_divida',
    )
    list_filter = (
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
        'concluido_divida',
    )
    list_display = (
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
        'concluido_divida',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ConveniosAditivos)
class ConveniosAditivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'convenio',
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
        'convenio',
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
        'convenio',
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



@admin.register(ConveniosArquivos)
class ConveniosArquivosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'convenio',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_filter = (
        'convenio',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    list_display = (
        'convenio',
        'nome_arquivo',
        'tipo',
        'descricao',
        'arquivo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ConveniosContasControle)
class ConveniosContasControleAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'convenio',
        'conta_controle',
    )
    list_filter = (
        'convenio',
        'conta_controle',
    )
    list_display = (
        'convenio',
        'conta_controle',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(ConveniosCronogramaMensal)
class ConveniosCronogramaMensalAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'ano',
        'convenio',
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
        'convenio',
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
        'convenio',
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



@admin.register(ConveniosDotacoes)
class ConveniosDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'convenio',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_filter = (
        'convenio',
        'orcamento',
        'dotacao',
        'valor',
    )
    list_display = (
        'convenio',
        'orcamento',
        'dotacao',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]