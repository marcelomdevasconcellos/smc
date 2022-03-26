# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    Licitacoes,
    LicitacoesDotacoes,
    Dispensas,
    DispensasDotacoes,
    Inexigibilidades,
    InexigibilidadesDotacoes,
)



@admin.register(Licitacoes)
class LicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome_orgao_ata',
        'cpf_gestor',
        'numero_licitacao',
        'tipo_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'nome_responsavel_juridico',
        'cpf_responsavel_juridico',
        'nome_responsavel_homologacao',
        'cpf_responsavel_homologacao',
        'numero_comissao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'hora_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    list_filter = (
        'nome_orgao_ata',
        'cpf_gestor',
        'numero_licitacao',
        'tipo_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'nome_responsavel_juridico',
        'cpf_responsavel_juridico',
        'nome_responsavel_homologacao',
        'cpf_responsavel_homologacao',
        'numero_comissao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'hora_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    list_display = (
        'nome_orgao_ata',
        'cpf_gestor',
        'numero_licitacao',
        'tipo_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'nome_responsavel_juridico',
        'cpf_responsavel_juridico',
        'nome_responsavel_homologacao',
        'cpf_responsavel_homologacao',
        'numero_comissao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'hora_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(LicitacoesDotacoes)
class LicitacoesDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'licitacao',
        'orcamento_despesa',
    )
    list_filter = (
        'licitacao',
        'orcamento_despesa',
    )
    list_display = (
        'licitacao',
        'orcamento_despesa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Dispensas)
class DispensasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    list_filter = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    list_display = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DispensasDotacoes)
class DispensasDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'dispensa',
        'orcamento_despesa',
    )
    list_filter = (
        'dispensa',
        'orcamento_despesa',
    )
    list_display = (
        'dispensa',
        'orcamento_despesa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Inexigibilidades)
class InexigibilidadesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    list_filter = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    list_display = (
        'credor',
        'numero',
        'dispositivo_legal',
        'num_processo',
        'descricao',
        'valor',
        'arquivo',
        'data_publicacao',
        'num_pagina_diario_oficial',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(InexigibilidadesDotacoes)
class InexigibilidadesDotacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'inexigibilidade',
        'orcamento_despesa',
    )
    list_filter = (
        'inexigibilidade',
        'orcamento_despesa',
    )
    list_display = (
        'inexigibilidade',
        'orcamento_despesa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]