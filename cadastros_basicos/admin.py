# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    ArquivosTipos,
    DatasReferencia,
    DespesasTipo,
    DispositivosLegais,
    Itens,
    Estados,
    Municipios,
    RetencoesTipos,
    Responsaveis,
    Setores,
)



@admin.register(ArquivosTipos)
class ArquivosTiposAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'titulo',
        'referencia',
    )
    list_filter = (
        'titulo',
        'referencia',
    )
    list_display = (
        'titulo',
        'referencia',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DatasReferencia)
class DatasReferenciaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'ano',
    )
    list_filter = (
        'codigo',
        'mes',
        'ano',
    )
    list_display = (
        'codigo',
        'mes',
        'ano',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(DespesasTipo)
class DespesasTipoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
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



@admin.register(DispositivosLegais)
class DispositivosLegaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
    )
    list_filter = (
        'tipo',
        'titulo',
    )
    list_display = (
        'tipo',
        'codigo',
        'titulo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Itens)
class ItensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento',
        'codigo',
        'titulo',
    )
    list_filter = (
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



@admin.register(Estados)
class EstadosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'sigla',
        'nome',
    )
    list_filter = (
        'nome',
    )
    list_display = (
        'sigla',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Municipios)
class MunicipiosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'estado',
        'nome',
        'cidade_uf',
        'codigo_tcm',
        'codigo_ibge',
    )
    list_filter = (
        'estado',
        'nome',
        'cidade_uf',
        'codigo_tcm',
        'codigo_ibge',
    )
    list_display = (
        'estado',
        'nome',
        'cidade_uf',
        'codigo_tcm',
        'codigo_ibge',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(RetencoesTipos)
class RetencoesTiposAdmin(AuditoriaAdmin):
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



@admin.register(Responsaveis)
class ResponsaveisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'cpf',
        'telefone',
        'email',
    )
    list_filter = (
        'nome',
        'cpf',
        'telefone',
        'email',
    )
    list_display = (
        'nome',
        'cpf',
        'telefone',
        'email',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Setores)
class SetoresAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'sigla',
    )
    list_filter = (
        'nome',
        'sigla',
    )
    list_display = (
        'nome',
        'sigla',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]