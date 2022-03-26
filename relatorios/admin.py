# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    Relatorios,
)



@admin.register(Relatorios)
class RelatoriosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'titulo',
        'campos',
        'sql',
    )
    list_filter = (
        'titulo',
        'campos',
        'sql',
    )
    list_display = (
        'titulo',
        'campos',
        'sql',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]