# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    Credores,
    Empenhos,
    Liquidacoes,
    Pagamentos,
    OrcamentosExecucaoDespesas,
    OrcamentosExecucaoDespesasMensais,
    OrcamentosExecucaoReceitas,
    OrcamentosExecucaoReceitasMensais,
)



@admin.register(Credores)
class CredoresAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'codigo',
        'cpf_cnpj',
        'telefone',
        'email',
        'cep',
        'logradouro',
        'numero',
        'municipio',
        'bairro',
        'uf',
        'status',
        'cod_contribuinte',
        'cod_municipio',
    )
    list_filter = (
        'nome',
        'codigo',
        'cpf_cnpj',
        'telefone',
        'email',
        'cep',
        'logradouro',
        'numero',
        'municipio',
        'bairro',
        'uf',
        'status',
        'cod_contribuinte',
        'cod_municipio',
    )
    list_display = (
        'nome',
        'codigo',
        'cpf_cnpj',
        'telefone',
        'email',
        'cep',
        'logradouro',
        'numero',
        'municipio',
        'bairro',
        'uf',
        'status',
        'cod_contribuinte',
        'cod_municipio',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Empenhos)
class EmpenhosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'cep_negociante',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_negociante',
        'cpf_gestor_contrato',
        'cd_cpf_gestor',
        'data_emissao_empenho',
        'data_emissao_empenho_substituto',
        'data_realizacao_licitacao',
        'data_referencia_empenho',
        'data_contrato',
        'descricao_empenho',
        'endereco_negociante',
        'estado_empenho',
        'modalidade_empenho',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_nota_anulacao',
        'numero_contrato',
        'numero_documento_negociante',
        'numero_empenho',
        'numero_empenho_substituto',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'fone_negociante',
        'tipo_fonte',
        'tipo_processo_licitatorio',
        'codigo_uf',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_empenhado',
    )
    list_filter = (
        'exercicio_orcamento',
        'cep_negociante',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_negociante',
        'cpf_gestor_contrato',
        'cd_cpf_gestor',
        'data_emissao_empenho',
        'data_emissao_empenho_substituto',
        'data_realizacao_licitacao',
        'data_referencia_empenho',
        'data_contrato',
        'descricao_empenho',
        'endereco_negociante',
        'estado_empenho',
        'modalidade_empenho',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_nota_anulacao',
        'numero_contrato',
        'numero_documento_negociante',
        'numero_empenho',
        'numero_empenho_substituto',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'fone_negociante',
        'tipo_fonte',
        'tipo_processo_licitatorio',
        'codigo_uf',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_empenhado',
    )
    list_display = (
        'exercicio_orcamento',
        'cep_negociante',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_negociante',
        'cpf_gestor_contrato',
        'cd_cpf_gestor',
        'data_emissao_empenho',
        'data_emissao_empenho_substituto',
        'data_realizacao_licitacao',
        'data_referencia_empenho',
        'data_contrato',
        'descricao_empenho',
        'endereco_negociante',
        'estado_empenho',
        'modalidade_empenho',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_nota_anulacao',
        'numero_contrato',
        'numero_documento_negociante',
        'numero_empenho',
        'numero_empenho_substituto',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'fone_negociante',
        'tipo_fonte',
        'tipo_processo_licitatorio',
        'codigo_uf',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_empenhado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Liquidacoes)
class LiquidacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'empenho',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_responsavel_liquidacao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia_liquidacao',
        'estado_folha',
        'estado_de_estorno',
        'nome_responsavel_liquidacao',
        'numero_empenho',
        'numero_sub_empenho_liquidacao',
        'valor_liquidado',
    )
    list_filter = (
        'empenho',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_responsavel_liquidacao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia_liquidacao',
        'estado_folha',
        'estado_de_estorno',
        'nome_responsavel_liquidacao',
        'numero_empenho',
        'numero_sub_empenho_liquidacao',
        'valor_liquidado',
    )
    list_display = (
        'empenho',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_responsavel_liquidacao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia_liquidacao',
        'estado_folha',
        'estado_de_estorno',
        'nome_responsavel_liquidacao',
        'numero_empenho',
        'numero_sub_empenho_liquidacao',
        'valor_liquidado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Pagamentos)
class PagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'liquidacao',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_pagador',
        'data_nota_pagamento',
        'data_emissao_empenho',
        'data_referencia',
        'estado_de_estornado',
        'nome_pagador',
        'numero_nota_pagamento',
        'nu_documento_caixa',
        'numero_empenho',
        'numero_sub_empenho',
        'valor_nota_pagamento',
        'valor_empenhado_a_pagar',
    )
    list_filter = (
        'liquidacao',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_pagador',
        'data_nota_pagamento',
        'data_emissao_empenho',
        'data_referencia',
        'estado_de_estornado',
        'nome_pagador',
        'numero_nota_pagamento',
        'nu_documento_caixa',
        'numero_empenho',
        'numero_sub_empenho',
        'valor_nota_pagamento',
        'valor_empenhado_a_pagar',
    )
    list_display = (
        'liquidacao',
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'cpf_pagador',
        'data_nota_pagamento',
        'data_emissao_empenho',
        'data_referencia',
        'estado_de_estornado',
        'nome_pagador',
        'numero_nota_pagamento',
        'nu_documento_caixa',
        'numero_empenho',
        'numero_sub_empenho',
        'valor_nota_pagamento',
        'valor_empenhado_a_pagar',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosExecucaoDespesas)
class OrcamentosExecucaoDespesasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento_despesas',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    list_filter = (
        'orcamento_despesas',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    list_display = (
        'orcamento_despesas',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosExecucaoDespesasMensais)
class OrcamentosExecucaoDespesasMensaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento_despesas',
        'mes',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    list_filter = (
        'orcamento_despesas',
        'mes',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    list_display = (
        'orcamento_despesas',
        'mes',
        'valor_dotacao_suplementado',
        'valor_dotacao_anulado',
        'valor_empenhado',
        'valor_empenhado_anulado',
        'valor_liquidado',
        'valor_liquidado_extornado',
        'valor_pago',
        'valor_pago_extornado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosExecucaoReceitas)
class OrcamentosExecucaoReceitasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento_receitas',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    list_filter = (
        'orcamento_receitas',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    list_display = (
        'orcamento_receitas',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(OrcamentosExecucaoReceitasMensais)
class OrcamentosExecucaoReceitasMensaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'orcamento_receitas',
        'mes',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    list_filter = (
        'orcamento_receitas',
        'mes',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    list_display = (
        'orcamento_receitas',
        'mes',
        'valor_arrecadado',
        'valor_arrecadacao_anulado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]