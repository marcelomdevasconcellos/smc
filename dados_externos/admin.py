# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from datetime import datetime
import requests

from django.contrib import admin
from django.forms import Select, Textarea
from django.utils.html import format_html
from config.mixins import AuditoriaAdmin, AuditoriaAdminTabularInline, AuditoriaAdminStackedInline

from .models import (
    TcmAgentesPublicos,
    TcmAnulacoesEmpenhos,
    TcmAnulacoesTaloesExtras,
    TcmAnulacoesTaloesReceitas,
    TcmBalanceteDespesaExtraOrcamentaria,
    TcmBalanceteDespesaOrcamentaria,
    TcmBalanceteReceitaExtraOrcamentaria,
    TcmBalanceteReceitaOrcamentaria,
    TcmBensMunicipios,
    TcmChequesNotasPagamentos,
    TcmClassificacao,
    TcmComissoesLicitacoes,
    TcmContasBancarias,
    TcmContasExtraOrcamentarias,
    TcmContratados,
    TcmContratos,
    TcmCpfCnpj,
    TcmCreditosAdicionais,
    TcmDadosOrcamentos,
    TcmDadosPessoais,
    TcmDespesaCategoriaEconomica,
    TcmDespesaElementoProjeto,
    TcmDespesaProjetoAtividade,
    TcmDespesasExtraOrcamentaria,
    TcmDestinoRealocacoesOrcamentarias,
    TcmDotacoesLicitacoes,
    TcmEmpenhosBens,
    TcmEstornosLiquidacoes,
    TcmEstornosPagamentos,
    TcmFontesAnulacao,
    TcmFuncoes,
    TcmGestores,
    TcmGestoresUnidadesGestoras,
    TcmGrupos,
    TcmItensLicitacoes,
    TcmItensNotasFiscais,
    TcmItensRemuneratorios,
    TcmLicitacoes,
    TcmLicitantes,
    TcmLiquidacoes,
    TcmMetodos,
    TcmMovimentacoesFontes,
    TcmMunicipios,
    TcmNegociantes,
    TcmNotasEmpenhos,
    TcmNotasFiscais,
    TcmNotasFiscaisLiquid,
    TcmNotasPagamentos,
    TcmOrcamentoReceita,
    TcmOrdenadores,
    TcmOrgaos,
    TcmParametros,
    TcmProcessosGestores,
    TcmProgramas,
    TcmPublicacoesEditaisLicitacoes,
    TcmRealocacoesOrcamentarias,
    TcmReavalBaixasBens,
    TcmRecursosEmpenhos,
    TcmTaloesExtras,
    TcmTaloesReceitas,
    TcmTipos,
    TcmTiposUnidadesAdministrativas,
    TcmUnidadeOrcamentariaBens,
    TcmUnidadesFederacao,
    TcmUnidadesGestoras,
    TcmUnidadesOrcamentarias,
    AspecEmpenhos,
    AspecEmpenhosMovimentos,
    AspecLiquidacoes,
    AspecLiquidacoesItens,
    AspecPagamentos,
    AspecPagamentosDetalhes,
)



@admin.register(TcmAgentesPublicos)
class TcmAgentesPublicosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_ocupacao_cbo',
        'codigo_amparo_legal',
        'codigo_expediente',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa_social',
        'codigo_regime_juridico',
        'codigo_regime_previdencia',
        'codigo_vinculo',
        'cpf_servidor',
        'data_posse',
        'data_publicacao_amparo_legal',
        'data_referencia_agente_publico',
        'data_amparo_legal',
        'data_expediente',
        'nome_servidor',
        'numero_matricula',
        'numero_dependentes',
        'numero_amparo_legal',
        'numero_expediente_nomeacao',
        'situacao_funcional',
        'tipo_cargo',
        'tipo_programa_social',
        'valor_carga_horaria',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_ocupacao_cbo',
        'codigo_amparo_legal',
        'codigo_expediente',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa_social',
        'codigo_regime_juridico',
        'codigo_regime_previdencia',
        'codigo_vinculo',
        'cpf_servidor',
        'data_posse',
        'data_publicacao_amparo_legal',
        'data_referencia_agente_publico',
        'data_amparo_legal',
        'data_expediente',
        'nome_servidor',
        'numero_matricula',
        'numero_dependentes',
        'numero_amparo_legal',
        'numero_expediente_nomeacao',
        'situacao_funcional',
        'tipo_cargo',
        'tipo_programa_social',
        'valor_carga_horaria',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_ocupacao_cbo',
        'codigo_amparo_legal',
        'codigo_expediente',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa_social',
        'codigo_regime_juridico',
        'codigo_regime_previdencia',
        'codigo_vinculo',
        'cpf_servidor',
        'data_posse',
        'data_publicacao_amparo_legal',
        'data_referencia_agente_publico',
        'data_amparo_legal',
        'data_expediente',
        'nome_servidor',
        'numero_matricula',
        'numero_dependentes',
        'numero_amparo_legal',
        'numero_expediente_nomeacao',
        'situacao_funcional',
        'tipo_cargo',
        'tipo_programa_social',
        'valor_carga_horaria',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmAnulacoesEmpenhos)
class TcmAnulacoesEmpenhosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_emissao_empenho',
        'data_referencia_anulacao',
        'descricao_anulacao',
        'modalidade_anulacao',
        'numero_anulacao',
        'numero_empenho',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_anulacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_emissao_empenho',
        'data_referencia_anulacao',
        'descricao_anulacao',
        'modalidade_anulacao',
        'numero_anulacao',
        'numero_empenho',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_anulacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_emissao_empenho',
        'data_referencia_anulacao',
        'descricao_anulacao',
        'modalidade_anulacao',
        'numero_anulacao',
        'numero_empenho',
        'valor_anterior_saldo_dotacao',
        'valor_atual_saldo_dotacao',
        'valor_anulacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmAnulacoesTaloesExtras)
class TcmAnulacoesTaloesExtrasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_conta',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'modalidade_anulacao',
        'numero_talao_receita',
        'valor_anulacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_conta',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'modalidade_anulacao',
        'numero_talao_receita',
        'valor_anulacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_conta',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'modalidade_anulacao',
        'numero_talao_receita',
        'valor_anulacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmAnulacoesTaloesReceitas)
class TcmAnulacoesTaloesReceitasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'md_anul_atr',
        'numero_talao_receita',
        'tipo_fonte',
        'valor_anulacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'md_anul_atr',
        'numero_talao_receita',
        'tipo_fonte',
        'valor_anulacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_anulacao',
        'data_referencia',
        'data_talao_receita',
        'historico_anulacao',
        'md_anul_atr',
        'numero_talao_receita',
        'tipo_fonte',
        'valor_anulacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmBalanceteDespesaExtraOrcamentaria)
class TcmBalanceteDespesaExtraOrcamentariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_anulacao_no_mes',
        'valor_anulacao_ate_mes',
        'valor_pago_no_mes',
        'valor_pago_ate_mes',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_anulacao_no_mes',
        'valor_anulacao_ate_mes',
        'valor_pago_no_mes',
        'valor_pago_ate_mes',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_anulacao_no_mes',
        'valor_anulacao_ate_mes',
        'valor_pago_no_mes',
        'valor_pago_ate_mes',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmBalanceteDespesaOrcamentaria)
class TcmBalanceteDespesaOrcamentariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_balancete',
        'tipo_fonte',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_nulacoes_dotacao_no_mes',
        'valor_anulacoes_empenhos_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
        'valor_estornos_liquidacao_no_mes',
        'valor_estornos_liquidacao_ate_mes',
        'valor_estornos_pagos_ate_mes',
        'valor_estornos_pagos_no_mes',
        'valor_saldo_dotacao',
        'valor_empenhado_pagar',
        'valor_empenhado_ate_mes',
        'valor_empenhado_no_mes',
        'valor_fixado_orcamento_bal_despesa',
        'valor_liquidado_ate_mes',
        'valor_liquidado_no_mes',
        'valor_pago_ate_mes',
        'valor_pago_no_mes',
        'valor_supl_ate_mes',
        'valor_supl_no_mes',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_balancete',
        'tipo_fonte',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_nulacoes_dotacao_no_mes',
        'valor_anulacoes_empenhos_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
        'valor_estornos_liquidacao_no_mes',
        'valor_estornos_liquidacao_ate_mes',
        'valor_estornos_pagos_ate_mes',
        'valor_estornos_pagos_no_mes',
        'valor_saldo_dotacao',
        'valor_empenhado_pagar',
        'valor_empenhado_ate_mes',
        'valor_empenhado_no_mes',
        'valor_fixado_orcamento_bal_despesa',
        'valor_liquidado_ate_mes',
        'valor_liquidado_no_mes',
        'valor_pago_ate_mes',
        'valor_pago_no_mes',
        'valor_supl_ate_mes',
        'valor_supl_no_mes',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_balancete',
        'tipo_fonte',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_nulacoes_dotacao_no_mes',
        'valor_anulacoes_empenhos_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
        'valor_estornos_liquidacao_no_mes',
        'valor_estornos_liquidacao_ate_mes',
        'valor_estornos_pagos_ate_mes',
        'valor_estornos_pagos_no_mes',
        'valor_saldo_dotacao',
        'valor_empenhado_pagar',
        'valor_empenhado_ate_mes',
        'valor_empenhado_no_mes',
        'valor_fixado_orcamento_bal_despesa',
        'valor_liquidado_ate_mes',
        'valor_liquidado_no_mes',
        'valor_pago_ate_mes',
        'valor_pago_no_mes',
        'valor_supl_ate_mes',
        'valor_supl_no_mes',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmBalanceteReceitaExtraOrcamentaria)
class TcmBalanceteReceitaExtraOrcamentariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_arrecadacao_empenhos_no_mes',
        'valor_arrecadacao_dotacao_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_arrecadacao_empenhos_no_mes',
        'valor_arrecadacao_dotacao_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'valor_nulacoes_dotacao_ate_mes',
        'valor_arrecadacao_empenhos_no_mes',
        'valor_arrecadacao_dotacao_ate_mes',
        'valor_anulacoes_empenhos_no_mes',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmBalanceteReceitaOrcamentaria)
class TcmBalanceteReceitaOrcamentariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'tipo_fonte',
        'valor_arrecadacao_ate_mes',
        'valor_arrecadacao_no_mes',
        'valor_anulacoes_ate_mes',
        'valor_anulacoes_no_mes',
        'valor_previsto_orcamento',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'tipo_fonte',
        'valor_arrecadacao_ate_mes',
        'valor_arrecadacao_no_mes',
        'valor_anulacoes_ate_mes',
        'valor_anulacoes_no_mes',
        'valor_previsto_orcamento',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_referencia',
        'tipo_balancete',
        'tipo_fonte',
        'valor_arrecadacao_ate_mes',
        'valor_arrecadacao_no_mes',
        'valor_anulacoes_ate_mes',
        'valor_anulacoes_no_mes',
        'valor_previsto_orcamento',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmBensMunicipios)
class TcmBensMunicipiosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'data_aquisicao_bem',
        'data_referencia_bem',
        'descricao_bem1',
        'descricao_bem2',
        'numero_registro_bem',
        'status_baixado_bem',
        'tipo_classificacao_bem',
        'tipo_natureza_bem',
    )
    list_filter = (
        'codigo_municipio',
        'data_aquisicao_bem',
        'data_referencia_bem',
        'descricao_bem1',
        'descricao_bem2',
        'numero_registro_bem',
        'status_baixado_bem',
        'tipo_classificacao_bem',
        'tipo_natureza_bem',
    )
    list_display = (
        'codigo_municipio',
        'data_aquisicao_bem',
        'data_referencia_bem',
        'descricao_bem1',
        'descricao_bem2',
        'numero_registro_bem',
        'status_baixado_bem',
        'tipo_classificacao_bem',
        'tipo_natureza_bem',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmChequesNotasPagamentos)
class TcmChequesNotasPagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_cheque',
        'data_emissao_empenho',
        'data_referencia_cheque',
        'nome_negociante_ng',
        'numero_agencia',
        'numero_conta',
        'numero_pagamento',
        'numero_banco',
        'numero_cheque',
        'numero_doc_ng',
        'numero_empenho',
        'tipo_documento_bancario',
        'valor_cheque',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_cheque',
        'data_emissao_empenho',
        'data_referencia_cheque',
        'nome_negociante_ng',
        'numero_agencia',
        'numero_conta',
        'numero_pagamento',
        'numero_banco',
        'numero_cheque',
        'numero_doc_ng',
        'numero_empenho',
        'tipo_documento_bancario',
        'valor_cheque',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_cheque',
        'data_emissao_empenho',
        'data_referencia_cheque',
        'nome_negociante_ng',
        'numero_agencia',
        'numero_conta',
        'numero_pagamento',
        'numero_banco',
        'numero_cheque',
        'numero_doc_ng',
        'numero_empenho',
        'tipo_documento_bancario',
        'valor_cheque',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmClassificacao)
class TcmClassificacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome_classificacao',
        'codigo_classificacao',
    )
    list_filter = (
        'nome_classificacao',
        'codigo_classificacao',
    )
    list_display = (
        'nome_classificacao',
        'codigo_classificacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmComissoesLicitacoes)
class TcmComissoesLicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'cpf_gestor',
        'data_criacao_comissao',
        'data_extincao_comissao',
        'numero_comissao',
        'numero_portaria_criacao',
        'numero_portaria_extincao',
        'tipo_comissao',
    )
    list_filter = (
        'codigo_municipio',
        'cpf_gestor',
        'data_criacao_comissao',
        'data_extincao_comissao',
        'numero_comissao',
        'numero_portaria_criacao',
        'numero_portaria_extincao',
        'tipo_comissao',
    )
    list_display = (
        'codigo_municipio',
        'cpf_gestor',
        'data_criacao_comissao',
        'data_extincao_comissao',
        'numero_comissao',
        'numero_portaria_criacao',
        'numero_portaria_extincao',
        'tipo_comissao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmContasBancarias)
class TcmContasBancariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_funcao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_abertura',
        'data_referencia',
        'descricao_objetivo',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'tipo_conta',
        'valor_saldo_abertura',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_funcao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_abertura',
        'data_referencia',
        'descricao_objetivo',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'tipo_conta',
        'valor_saldo_abertura',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_funcao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_abertura',
        'data_referencia',
        'descricao_objetivo',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'tipo_conta',
        'valor_saldo_abertura',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmContasExtraOrcamentarias)
class TcmContasExtraOrcamentariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_conta_extra_orc',
        'codigo_municipio',
        'data_referencia_doc',
        'desc_conta_extra_orc',
        'vl_saldo_ini',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_conta_extra_orc',
        'codigo_municipio',
        'data_referencia_doc',
        'desc_conta_extra_orc',
        'vl_saldo_ini',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_conta_extra_orc',
        'codigo_municipio',
        'data_referencia_doc',
        'desc_conta_extra_orc',
        'vl_saldo_ini',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmContratados)
class TcmContratadosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'cpf_gestor',
        'data_contrato',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_contrato',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    list_filter = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'cpf_gestor',
        'data_contrato',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_contrato',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    list_display = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'cpf_gestor',
        'data_contrato',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_contrato',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmContratos)
class TcmContratosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'cpf_gestor',
        'data_inicio_vigencia_contrato',
        'data_fim_vigencia_contrato',
        'data_contrato',
        'data_contrato_original',
        'descricao_objeto_contrato',
        'modalidade_contrato',
        'numero_contrato',
        'numero_contrato_original',
        'tipo_contrato',
        'valor_total_contrato',
    )
    list_filter = (
        'codigo_municipio',
        'cpf_gestor',
        'data_inicio_vigencia_contrato',
        'data_fim_vigencia_contrato',
        'data_contrato',
        'data_contrato_original',
        'descricao_objeto_contrato',
        'modalidade_contrato',
        'numero_contrato',
        'numero_contrato_original',
        'tipo_contrato',
        'valor_total_contrato',
    )
    list_display = (
        'codigo_municipio',
        'cpf_gestor',
        'data_inicio_vigencia_contrato',
        'data_fim_vigencia_contrato',
        'data_contrato',
        'data_contrato_original',
        'descricao_objeto_contrato',
        'modalidade_contrato',
        'numero_contrato',
        'numero_contrato_original',
        'tipo_contrato',
        'valor_total_contrato',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmCpfCnpj)
class TcmCpfCnpjAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_cnpj_cpf',
        'nome',
    )
    list_filter = (
        'codigo_cnpj_cpf',
        'nome',
    )
    list_display = (
        'codigo_cnpj_cpf',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmCreditosAdicionais)
class TcmCreditosAdicionaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte_recursos',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'cd_elemento_despesa',
        'data_abertura_credito',
        'data_referencia_doc',
        'numero_lei',
        'numero_decreto',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_abertura_credito',
        'tipo_fonte',
        'valor_credito_anulacao',
        'valor_credito_excesso',
        'valor_credito_operacao',
        'valor_credito_super',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte_recursos',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'cd_elemento_despesa',
        'data_abertura_credito',
        'data_referencia_doc',
        'numero_lei',
        'numero_decreto',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_abertura_credito',
        'tipo_fonte',
        'valor_credito_anulacao',
        'valor_credito_excesso',
        'valor_credito_operacao',
        'valor_credito_super',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte_recursos',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'cd_elemento_despesa',
        'data_abertura_credito',
        'data_referencia_doc',
        'numero_lei',
        'numero_decreto',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_abertura_credito',
        'tipo_fonte',
        'valor_credito_anulacao',
        'valor_credito_excesso',
        'valor_credito_operacao',
        'valor_credito_super',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDadosOrcamentos)
class TcmDadosOrcamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_municipio',
        'data_aprov_loa',
        'data_envio_loa',
        'data_public_loa',
        'nu_lei_orcamento',
        'numero_perc_sup_orcamento',
        'valor_total_fixado_orcamento',
        'valor_total_supl_orcamento',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_municipio',
        'data_aprov_loa',
        'data_envio_loa',
        'data_public_loa',
        'nu_lei_orcamento',
        'numero_perc_sup_orcamento',
        'valor_total_fixado_orcamento',
        'valor_total_supl_orcamento',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_municipio',
        'data_aprov_loa',
        'data_envio_loa',
        'data_public_loa',
        'nu_lei_orcamento',
        'numero_perc_sup_orcamento',
        'valor_total_fixado_orcamento',
        'valor_total_supl_orcamento',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDadosPessoais)
class TcmDadosPessoaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'cpf_servidor',
        'data_nascimento_servidor',
        'nome_mae',
        'nome_pai',
        'nome_servidor',
        'nu_identidade',
    )
    list_filter = (
        'cpf_servidor',
        'data_nascimento_servidor',
        'nome_mae',
        'nome_pai',
        'nome_servidor',
        'nu_identidade',
    )
    list_display = (
        'cpf_servidor',
        'data_nascimento_servidor',
        'nome_mae',
        'nome_pai',
        'nome_servidor',
        'nu_identidade',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDespesaCategoriaEconomica)
class TcmDespesaCategoriaEconomicaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'nome_elemento_despesa',
        'valor_total_fixado',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'nome_elemento_despesa',
        'valor_total_fixado',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'nome_elemento_despesa',
        'valor_total_fixado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDespesaElementoProjeto)
class TcmDespesaElementoProjetoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_atual_categoria_economica',
        'valor_orcado_categoria_economica',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_atual_categoria_economica',
        'valor_orcado_categoria_economica',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_atual_categoria_economica',
        'valor_orcado_categoria_economica',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDespesaProjetoAtividade)
class TcmDespesaProjetoAtividadeAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_orcamento',
        'descricao_projeto_atividade',
        'nome_projeto_atividade',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'valor_total_fixado_projeto_atividade',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_orcamento',
        'descricao_projeto_atividade',
        'nome_projeto_atividade',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'valor_total_fixado_projeto_atividade',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'codigo_tipo_orcamento',
        'descricao_projeto_atividade',
        'nome_projeto_atividade',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'valor_total_fixado_projeto_atividade',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDespesasExtraOrcamentaria)
class TcmDespesasExtraOrcamentariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_despesa_extra',
        'data_referencia_documentacao',
        'nome_credor_despesa_extra',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'numero_documento_caixa',
        'numero_documento_despesa_extra',
        'status_estorno_despesa_extra',
        'tipo_documento_despesa_extra',
        'valor_deducao_despesa_extra',
        'valor_documento_despesa_extra',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_despesa_extra',
        'data_referencia_documentacao',
        'nome_credor_despesa_extra',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'numero_documento_caixa',
        'numero_documento_despesa_extra',
        'status_estorno_despesa_extra',
        'tipo_documento_despesa_extra',
        'valor_deducao_despesa_extra',
        'valor_documento_despesa_extra',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_conta_extraorcamentaria',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_despesa_extra',
        'data_referencia_documentacao',
        'nome_credor_despesa_extra',
        'numero_agencia',
        'numero_conta',
        'numero_banco',
        'numero_documento_caixa',
        'numero_documento_despesa_extra',
        'status_estorno_despesa_extra',
        'tipo_documento_despesa_extra',
        'valor_deducao_despesa_extra',
        'valor_documento_despesa_extra',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDestinoRealocacoesOrcamentarias)
class TcmDestinoRealocacoesOrcamentariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'valor_destino',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'valor_destino',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'valor_destino',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmDotacoesLicitacoes)
class TcmDotacoesLicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_realizacao_licitacao',
        'numero_licitacao',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_dotacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_realizacao_licitacao',
        'numero_licitacao',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_dotacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_realizacao_licitacao',
        'numero_licitacao',
        'numero_projeto_atividade',
        'numero_subprojeto_atividade',
        'tipo_fonte',
        'valor_dotacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmEmpenhosBens)
class TcmEmpenhosBensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_referencia',
        'numero_nota_empenho',
        'numero_registro_bem',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_referencia',
        'numero_nota_empenho',
        'numero_registro_bem',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_referencia',
        'numero_nota_empenho',
        'numero_registro_bem',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmEstornosLiquidacoes)
class TcmEstornosLiquidacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_liquidacao',
        'data_liquidacao',
        'data_referencia_estorno_liquidacao',
        'descricao_justificativa',
        'nome_assessor',
        'numero_empenho',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_liquidacao',
        'data_liquidacao',
        'data_referencia_estorno_liquidacao',
        'descricao_justificativa',
        'nome_assessor',
        'numero_empenho',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_liquidacao',
        'data_liquidacao',
        'data_referencia_estorno_liquidacao',
        'descricao_justificativa',
        'nome_assessor',
        'numero_empenho',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmEstornosPagamentos)
class TcmEstornosPagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_pagamento',
        'data_referencia_estorno_pagamento',
        'descricao_justificativa',
        'nome_assessor',
        'numero_pagamento',
        'numero_empenho',
        'numero_sub_empenho_nota_pagamento',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_pagamento',
        'data_referencia_estorno_pagamento',
        'descricao_justificativa',
        'nome_assessor',
        'numero_pagamento',
        'numero_empenho',
        'numero_sub_empenho_nota_pagamento',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_empenho',
        'data_estorno_pagamento',
        'data_referencia_estorno_pagamento',
        'descricao_justificativa',
        'nome_assessor',
        'numero_pagamento',
        'numero_empenho',
        'numero_sub_empenho_nota_pagamento',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmFontesAnulacao)
class TcmFontesAnulacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_abertura_credito',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_fonte',
        'valor_fonte_anul',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_abertura_credito',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_fonte',
        'valor_fonte_anul',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade_orcamentaria',
        'codigo_elemento_despesa',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_abertura_credito',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_abertura_credito_dia',
        'tipo_fonte',
        'valor_fonte_anul',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmFuncoes)
class TcmFuncoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_funcao',
        'nome_funcao',
    )
    list_filter = (
        'codigo_funcao',
        'nome_funcao',
    )
    list_display = (
        'codigo_funcao',
        'nome_funcao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmGestores)
class TcmGestoresAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'nome',
    )
    list_filter = (
        'codigo',
        'nome',
    )
    list_display = (
        'codigo',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmGestoresUnidadesGestoras)
class TcmGestoresUnidadesGestorasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inicio_gestao',
        'data_referencia',
        'data_fim_gestao',
        'nome_gestor',
        'numero_expediente',
        'status_ordenador_despesa',
        'tipo_cargo',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inicio_gestao',
        'data_referencia',
        'data_fim_gestao',
        'nome_gestor',
        'numero_expediente',
        'status_ordenador_despesa',
        'tipo_cargo',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inicio_gestao',
        'data_referencia',
        'data_fim_gestao',
        'nome_gestor',
        'numero_expediente',
        'status_ordenador_despesa',
        'tipo_cargo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmGrupos)
class TcmGruposAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'descricao',
        'nome',
        'ordem',
    )
    list_filter = (
        'codigo',
        'descricao',
        'nome',
        'ordem',
    )
    list_display = (
        'codigo',
        'descricao',
        'nome',
        'ordem',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmItensLicitacoes)
class TcmItensLicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'descricao_unidade_item_licitacao',
        'descricao_item_licitacao',
        'numero_licitacao',
        'numero_quantidade_item_licitacao',
        'numero_documento_negociante',
        'numero_sequencial_item_licitacao',
        'valor_unitario_item_licitacao',
        'valor_vencedor_item_licitacao',
    )
    list_filter = (
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'descricao_unidade_item_licitacao',
        'descricao_item_licitacao',
        'numero_licitacao',
        'numero_quantidade_item_licitacao',
        'numero_documento_negociante',
        'numero_sequencial_item_licitacao',
        'valor_unitario_item_licitacao',
        'valor_vencedor_item_licitacao',
    )
    list_display = (
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'descricao_unidade_item_licitacao',
        'descricao_item_licitacao',
        'numero_licitacao',
        'numero_quantidade_item_licitacao',
        'numero_documento_negociante',
        'numero_sequencial_item_licitacao',
        'valor_unitario_item_licitacao',
        'valor_vencedor_item_licitacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmItensNotasFiscais)
class TcmItensNotasFiscaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'exercicio_orcamento',
        'codigo_orgao',
        'codigo_unidade',
        'data_emissao',
        'numero_nota_empenho',
        'data_liquidacao',
        'tipo_nota_fiscal',
        'numero_nota_fiscal',
        'numero_item_sequencial',
        'descricao1_item',
        'descricao2_item',
        'unidade_compra',
        'numero_quantidade_comprada',
        'valor_unitario_item',
        'valor_total_item',
        'codigo_ncm',
    )
    list_filter = (
        'codigo_municipio',
        'exercicio_orcamento',
        'codigo_orgao',
        'codigo_unidade',
        'data_emissao',
        'numero_nota_empenho',
        'data_liquidacao',
        'tipo_nota_fiscal',
        'numero_nota_fiscal',
        'numero_item_sequencial',
        'descricao1_item',
        'descricao2_item',
        'unidade_compra',
        'numero_quantidade_comprada',
        'valor_unitario_item',
        'valor_total_item',
        'codigo_ncm',
    )
    list_display = (
        'codigo_municipio',
        'exercicio_orcamento',
        'codigo_orgao',
        'codigo_unidade',
        'data_emissao',
        'numero_nota_empenho',
        'data_liquidacao',
        'tipo_nota_fiscal',
        'numero_nota_fiscal',
        'numero_item_sequencial',
        'descricao1_item',
        'descricao2_item',
        'unidade_compra',
        'numero_quantidade_comprada',
        'valor_unitario_item',
        'valor_total_item',
        'codigo_ncm',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmItensRemuneratorios)
class TcmItensRemuneratoriosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_amparo_legal',
        'codigo_item',
        'codigo_municipio',
        'data_publicacao',
        'data_publicacao_decreto',
        'data_referencia',
        'data_amparo_legal',
        'data_decreto',
        'descricao_item',
        'numeto_amparo_legal',
        'numero_decreto',
        'st_extinto_ir',
        'tipo_classificacao',
        'tipo_item',
    )
    list_filter = (
        'codigo_amparo_legal',
        'codigo_item',
        'codigo_municipio',
        'data_publicacao',
        'data_publicacao_decreto',
        'data_referencia',
        'data_amparo_legal',
        'data_decreto',
        'descricao_item',
        'numeto_amparo_legal',
        'numero_decreto',
        'st_extinto_ir',
        'tipo_classificacao',
        'tipo_item',
    )
    list_display = (
        'codigo_amparo_legal',
        'codigo_item',
        'codigo_municipio',
        'data_publicacao',
        'data_publicacao_decreto',
        'data_referencia',
        'data_amparo_legal',
        'data_decreto',
        'descricao_item',
        'numeto_amparo_legal',
        'numero_decreto',
        'st_extinto_ir',
        'tipo_classificacao',
        'tipo_item',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmLicitacoes)
class TcmLicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'cpf_gestor',
        'cpf_responsavel_juridico',
        'cpf_responsavel_homologacao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'hora_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'nome_orgao_ata',
        'nome_responsavel_juridico',
        'nome_responsavel_homologacao',
        'numero_comissao',
        'numero_licitacao',
        'tipo_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    list_filter = (
        'codigo_municipio',
        'cpf_gestor',
        'cpf_responsavel_juridico',
        'cpf_responsavel_homologacao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'hora_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'nome_orgao_ata',
        'nome_responsavel_juridico',
        'nome_responsavel_homologacao',
        'numero_comissao',
        'numero_licitacao',
        'tipo_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    list_display = (
        'codigo_municipio',
        'cpf_gestor',
        'cpf_responsavel_juridico',
        'cpf_responsavel_homologacao',
        'data_criacao_comissao',
        'data_emissao_edital',
        'data_homologacao',
        'data_realizacao_autuacao_licitacao',
        'data_realizacao_licitacao',
        'descricao1_motivo_fornecedor',
        'descricao2_motivo_fornecedor',
        'descricao1_objeto_licitacao',
        'descricao2_objeto_licitacao',
        'descricao1_justificativa_preco',
        'descricao2_justificativa_preco',
        'hora_licitacao',
        'modalidade_licitacao',
        'modalidade_processo_administrativo',
        'nome_orgao_ata',
        'nome_responsavel_juridico',
        'nome_responsavel_homologacao',
        'numero_comissao',
        'numero_licitacao',
        'tipo_licitacao',
        'valor_limite_superior',
        'valor_orcado_estimado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmLicitantes)
class TcmLicitantesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    list_filter = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    list_display = (
        'cep_negociante',
        'codigo_municipio',
        'codigo_tipo_negociante',
        'data_realizacao_licitacao',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_licitacao',
        'numero_documento_negociante',
        'fone_negociante',
        'codigo_uf',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmLiquidacoes)
class TcmLiquidacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
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



@admin.register(TcmMetodos)
class TcmMetodosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'conexao',
        'descricao',
        'grupo',
        'nome',
    )
    list_filter = (
        'codigo',
        'conexao',
        'descricao',
        'grupo',
        'nome',
    )
    list_display = (
        'codigo',
        'conexao',
        'descricao',
        'grupo',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmMovimentacoesFontes)
class TcmMovimentacoesFontesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'exercicio_orcamento',
        'data_modificacao_fonte',
        'numero_modificacao_dia',
        'tipo_movimentacao',
        'codigo_orgao',
        'codigo_unidade',
        'funcao',
        'sub_funcao',
        'projeto_atividade',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'codigo_elemento_despesa',
        'grupo_fonte_origem',
        'codigo_fonte_origem',
        'grupo_fonte_destino',
        'codigo_fonte_destino',
        'valor_movimentacao_fonte',
        'data_referencia_movimentacao',
    )
    list_filter = (
        'codigo_municipio',
        'exercicio_orcamento',
        'data_modificacao_fonte',
        'numero_modificacao_dia',
        'tipo_movimentacao',
        'codigo_orgao',
        'codigo_unidade',
        'funcao',
        'sub_funcao',
        'projeto_atividade',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'codigo_elemento_despesa',
        'grupo_fonte_origem',
        'codigo_fonte_origem',
        'grupo_fonte_destino',
        'codigo_fonte_destino',
        'valor_movimentacao_fonte',
        'data_referencia_movimentacao',
    )
    list_display = (
        'codigo_municipio',
        'exercicio_orcamento',
        'data_modificacao_fonte',
        'numero_modificacao_dia',
        'tipo_movimentacao',
        'codigo_orgao',
        'codigo_unidade',
        'funcao',
        'sub_funcao',
        'projeto_atividade',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'codigo_elemento_despesa',
        'grupo_fonte_origem',
        'codigo_fonte_origem',
        'grupo_fonte_destino',
        'codigo_fonte_destino',
        'valor_movimentacao_fonte',
        'data_referencia_movimentacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmMunicipios)
class TcmMunicipiosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_municipio',
        'geoibgeid',
        'geonamesid',
        'nome_municipio',
    )
    list_filter = (
        'codigo_municipio',
        'geoibgeid',
        'geonamesid',
        'nome_municipio',
    )
    list_display = (
        'codigo_municipio',
        'geoibgeid',
        'geonamesid',
        'nome_municipio',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmNegociantes)
class TcmNegociantesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'cep_negociante',
        'codigo_tipo_negociante',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_documento_negociante',
        'fone_negociante',
        'uf_negociante',
    )
    list_filter = (
        'cep_negociante',
        'codigo_tipo_negociante',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_documento_negociante',
        'fone_negociante',
        'uf_negociante',
    )
    list_display = (
        'cep_negociante',
        'codigo_tipo_negociante',
        'endereco_negociante',
        'nome_municipio_negociante',
        'nome_negociante',
        'numero_documento_negociante',
        'fone_negociante',
        'uf_negociante',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmNotasEmpenhos)
class TcmNotasEmpenhosAdmin(AuditoriaAdmin):
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



@admin.register(TcmNotasFiscais)
class TcmNotasFiscaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'cgf_emitente',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia',
        'data_limite',
        'numero_nota_fiscal',
        'numero_serie',
        'numero_serie_selo_transito',
        'numero_empenho',
        'numero_formulario',
        'numero_protocolo_autenticacao',
        'numero_selo_transito',
        'tipo_emissao',
        'tipo_nota_fiscal',
        'valor_bruto',
        'valor_aliquota_iss',
        'valor_base_calculo_iss',
        'valor_desconto',
        'valor_liquido',
    )
    list_filter = (
        'exercicio_orcamento',
        'cgf_emitente',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia',
        'data_limite',
        'numero_nota_fiscal',
        'numero_serie',
        'numero_serie_selo_transito',
        'numero_empenho',
        'numero_formulario',
        'numero_protocolo_autenticacao',
        'numero_selo_transito',
        'tipo_emissao',
        'tipo_nota_fiscal',
        'valor_bruto',
        'valor_aliquota_iss',
        'valor_base_calculo_iss',
        'valor_desconto',
        'valor_liquido',
    )
    list_display = (
        'exercicio_orcamento',
        'cgf_emitente',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao',
        'data_emissao_empenho',
        'data_liquidacao',
        'data_referencia',
        'data_limite',
        'numero_nota_fiscal',
        'numero_serie',
        'numero_serie_selo_transito',
        'numero_empenho',
        'numero_formulario',
        'numero_protocolo_autenticacao',
        'numero_selo_transito',
        'tipo_emissao',
        'tipo_nota_fiscal',
        'valor_bruto',
        'valor_aliquota_iss',
        'valor_base_calculo_iss',
        'valor_desconto',
        'valor_liquido',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmNotasFiscaisLiquid)
class TcmNotasFiscaisLiquidAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'numero_cgf_emitente_nota_fiscal',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_nota_fiscal',
        'data_emissao_empenho',
        'data_liquidacao_nota_fiscal',
        'data_referencia_nota_fiscal',
        'data_limite_nota_fiscal',
        'nome_resp_liquidacao_nota_fiscal',
        'numero_nota_fiscal',
        'numero_serie_nota_fiscal',
        'numero_serie_transito_nota_fiscal',
        'numero_empenho',
        'numero_formulario_nota_fiscal',
        'numero_selo_transito_nota_fiscal',
        'numero_sub_empenho_nota_fiscal',
        'tipo_nota_fiscal',
        'uf_emitente_nota_fiscal',
        'valor_nota_fiscal',
    )
    list_filter = (
        'exercicio_orcamento',
        'numero_cgf_emitente_nota_fiscal',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_nota_fiscal',
        'data_emissao_empenho',
        'data_liquidacao_nota_fiscal',
        'data_referencia_nota_fiscal',
        'data_limite_nota_fiscal',
        'nome_resp_liquidacao_nota_fiscal',
        'numero_nota_fiscal',
        'numero_serie_nota_fiscal',
        'numero_serie_transito_nota_fiscal',
        'numero_empenho',
        'numero_formulario_nota_fiscal',
        'numero_selo_transito_nota_fiscal',
        'numero_sub_empenho_nota_fiscal',
        'tipo_nota_fiscal',
        'uf_emitente_nota_fiscal',
        'valor_nota_fiscal',
    )
    list_display = (
        'exercicio_orcamento',
        'numero_cgf_emitente_nota_fiscal',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_emissao_nota_fiscal',
        'data_emissao_empenho',
        'data_liquidacao_nota_fiscal',
        'data_referencia_nota_fiscal',
        'data_limite_nota_fiscal',
        'nome_resp_liquidacao_nota_fiscal',
        'numero_nota_fiscal',
        'numero_serie_nota_fiscal',
        'numero_serie_transito_nota_fiscal',
        'numero_empenho',
        'numero_formulario_nota_fiscal',
        'numero_selo_transito_nota_fiscal',
        'numero_sub_empenho_nota_fiscal',
        'tipo_nota_fiscal',
        'uf_emitente_nota_fiscal',
        'valor_nota_fiscal',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmNotasPagamentos)
class TcmNotasPagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
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



@admin.register(TcmOrcamentoReceita)
class TcmOrcamentoReceitaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'descricao_rubrica',
        'tipo_fonte',
        'valor_previsto',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'descricao_rubrica',
        'tipo_fonte',
        'valor_previsto',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'descricao_rubrica',
        'tipo_fonte',
        'valor_previsto',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmOrdenadores)
class TcmOrdenadoresAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inclusao_unidade_orcamentaria',
        'data_inicio_gestao_ordenador',
        'data_referencia_ordenador',
        'data_fim_gestao_ordenador',
        'nome_ordenador',
        'numero_expediente_nomeacao',
        'tipo_cargo',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inclusao_unidade_orcamentaria',
        'data_inicio_gestao_ordenador',
        'data_referencia_ordenador',
        'data_fim_gestao_ordenador',
        'nome_ordenador',
        'numero_expediente_nomeacao',
        'tipo_cargo',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade_gestora',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor',
        'data_inclusao_unidade_orcamentaria',
        'data_inicio_gestao_ordenador',
        'data_referencia_ordenador',
        'data_fim_gestao_ordenador',
        'nome_ordenador',
        'numero_expediente_nomeacao',
        'tipo_cargo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmOrgaos)
class TcmOrgaosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'cgc_orgao',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_orgao',
    )
    list_filter = (
        'exercicio_orcamento',
        'cgc_orgao',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_orgao',
    )
    list_display = (
        'exercicio_orcamento',
        'cgc_orgao',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_orgao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmParametros)
class TcmParametrosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'descricao',
        'entrada',
        'metodo',
        'nome',
        'requerido',
        'tipo',
    )
    list_filter = (
        'codigo',
        'descricao',
        'entrada',
        'metodo',
        'nome',
        'requerido',
        'tipo',
    )
    list_display = (
        'codigo',
        'descricao',
        'entrada',
        'metodo',
        'nome',
        'requerido',
        'tipo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmProcessosGestores)
class TcmProcessosGestoresAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio',
        'codigo_gestor',
        'codigo_municipio',
        'gestor',
        'municipio',
        'natureza_processo',
        'nota_improbidade',
        'processo',
    )
    list_filter = (
        'exercicio',
        'codigo_gestor',
        'codigo_municipio',
        'gestor',
        'municipio',
        'natureza_processo',
        'nota_improbidade',
        'processo',
    )
    list_display = (
        'exercicio',
        'codigo_gestor',
        'codigo_municipio',
        'gestor',
        'municipio',
        'natureza_processo',
        'nota_improbidade',
        'processo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmProgramas)
class TcmProgramasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_programa',
        'nome_programa',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_programa',
        'nome_programa',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_programa',
        'nome_programa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmPublicacoesEditaisLicitacoes)
class TcmPublicacoesEditaisLicitacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_publicacao_edital',
        'codigo_municipio',
        'data_publicacao_edital',
        'data_realizacao_licitacao',
        'descricao_publicacao_edital',
        'numero_licitacao',
        'numero_sequencial_publicacao_edital',
    )
    list_filter = (
        'codigo_publicacao_edital',
        'codigo_municipio',
        'data_publicacao_edital',
        'data_realizacao_licitacao',
        'descricao_publicacao_edital',
        'numero_licitacao',
        'numero_sequencial_publicacao_edital',
    )
    list_display = (
        'codigo_publicacao_edital',
        'codigo_municipio',
        'data_publicacao_edital',
        'data_realizacao_licitacao',
        'descricao_publicacao_edital',
        'numero_licitacao',
        'numero_sequencial_publicacao_edital',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmRealocacoesOrcamentarias)
class TcmRealocacoesOrcamentariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_lei',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'tipo_realocacao',
        'valor_realocado',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_lei',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'tipo_realocacao',
        'valor_realocado',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_projeto_atividade',
        'codigo_fonte',
        'codigo_funcao',
        'codigo_subfuncao',
        'codigo_unidade',
        'codigo_elemento',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_programa',
        'data_alteracao',
        'data_referencia',
        'numero_lei',
        'numero_projeto_atividade',
        'numero_sub_projeto_atividade',
        'numero_sequencia',
        'tipo_fonte',
        'tipo_realocacao',
        'valor_realocado',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmReavalBaixasBens)
class TcmReavalBaixasBensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_avaliacao',
        'data_referencia',
        'descricao_motivo',
        'numero_expediente',
        'numero_registro_bem',
        'status_situacao_bem',
        'valor_avaliacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_avaliacao',
        'data_referencia',
        'descricao_motivo',
        'numero_expediente',
        'numero_registro_bem',
        'status_situacao_bem',
        'valor_avaliacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_avaliacao',
        'data_referencia',
        'descricao_motivo',
        'numero_expediente',
        'numero_registro_bem',
        'status_situacao_bem',
        'valor_avaliacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmRecursosEmpenhos)
class TcmRecursosEmpenhosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_celebracao_convenio',
        'data_emissao_empenho',
        'numero_empenho',
        'numero_sequencial_recurso',
        'numero_sequencial_convenio',
        'tipo_recurso_empenho',
        'valor_recurso_empenho',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_celebracao_convenio',
        'data_emissao_empenho',
        'numero_empenho',
        'numero_sequencial_recurso',
        'numero_sequencial_convenio',
        'tipo_recurso_empenho',
        'valor_recurso_empenho',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'data_celebracao_convenio',
        'data_emissao_empenho',
        'numero_empenho',
        'numero_sequencial_recurso',
        'numero_sequencial_convenio',
        'tipo_recurso_empenho',
        'valor_recurso_empenho',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmTaloesExtras)
class TcmTaloesExtrasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'cd_conta_ctx',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tx',
        'dt_ref_tx',
        'dt_talao_receita_tx',
        'de_hist_receita_tx',
        'nu_agencia_bancaria_tx',
        'nu_conta_corrente_tx',
        'nu_banco_tx',
        'nu_doc_contrib_tx',
        'nu_doc_credito_tx',
        'nu_talao_receita_tx',
        'nm_razao_social_contrib_tx',
        'tp_doc_credito_tx',
        'tp_doc_contrib_tx',
        'vl_receita_tx',
    )
    list_filter = (
        'exercicio_orcamento',
        'cd_conta_ctx',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tx',
        'dt_ref_tx',
        'dt_talao_receita_tx',
        'de_hist_receita_tx',
        'nu_agencia_bancaria_tx',
        'nu_conta_corrente_tx',
        'nu_banco_tx',
        'nu_doc_contrib_tx',
        'nu_doc_credito_tx',
        'nu_talao_receita_tx',
        'nm_razao_social_contrib_tx',
        'tp_doc_credito_tx',
        'tp_doc_contrib_tx',
        'vl_receita_tx',
    )
    list_display = (
        'exercicio_orcamento',
        'cd_conta_ctx',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tx',
        'dt_ref_tx',
        'dt_talao_receita_tx',
        'de_hist_receita_tx',
        'nu_agencia_bancaria_tx',
        'nu_conta_corrente_tx',
        'nu_banco_tx',
        'nu_doc_contrib_tx',
        'nu_doc_credito_tx',
        'nu_talao_receita_tx',
        'nm_razao_social_contrib_tx',
        'tp_doc_credito_tx',
        'tp_doc_contrib_tx',
        'vl_receita_tx',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmTaloesReceitas)
class TcmTaloesReceitasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tr',
        'data_referencia',
        'data_talao_receita',
        'historico_receita',
        'numero_agencia_bancaria',
        'numero_conta_corrente',
        'numero_banco',
        'numero_doc_credito',
        'numero_doc_contribuinte',
        'numero_talao_receita',
        'nome_razao_social_contribuinte',
        'tipo_doc_credito',
        'tipo_doc_contribuinte',
        'tipo_fonte',
        'valor_receita',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tr',
        'data_referencia',
        'data_talao_receita',
        'historico_receita',
        'numero_agencia_bancaria',
        'numero_conta_corrente',
        'numero_banco',
        'numero_doc_credito',
        'numero_doc_contribuinte',
        'numero_talao_receita',
        'nome_razao_social_contribuinte',
        'tipo_doc_credito',
        'tipo_doc_contribuinte',
        'tipo_fonte',
        'valor_receita',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_fonte',
        'codigo_rubrica',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'dt_credito_tr',
        'data_referencia',
        'data_talao_receita',
        'historico_receita',
        'numero_agencia_bancaria',
        'numero_conta_corrente',
        'numero_banco',
        'numero_doc_credito',
        'numero_doc_contribuinte',
        'numero_talao_receita',
        'nome_razao_social_contribuinte',
        'tipo_doc_credito',
        'tipo_doc_contribuinte',
        'tipo_fonte',
        'valor_receita',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmTipos)
class TcmTiposAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'descricao',
        'nome',
    )
    list_filter = (
        'codigo',
        'descricao',
        'nome',
    )
    list_display = (
        'codigo',
        'descricao',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmTiposUnidadesAdministrativas)
class TcmTiposUnidadesAdministrativasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_tipo_unidade_administrativa',
        'nome_tipo_unidade_administrativa',
    )
    list_filter = (
        'codigo_tipo_unidade_administrativa',
        'nome_tipo_unidade_administrativa',
    )
    list_display = (
        'codigo_tipo_unidade_administrativa',
        'nome_tipo_unidade_administrativa',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmUnidadeOrcamentariaBens)
class TcmUnidadeOrcamentariaBensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_disponibilizacao',
        'data_referencia',
        'numero_expediente',
        'numero_registro_bem',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_disponibilizacao',
        'data_referencia',
        'numero_expediente',
        'numero_registro_bem',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_ingresso',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_vinculo',
        'cpf_servidor_municipal',
        'data_disponibilizacao',
        'data_referencia',
        'numero_expediente',
        'numero_registro_bem',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmUnidadesFederacao)
class TcmUnidadesFederacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_unidade_federacao',
        'nome_unidade_federacao',
        'sigla_unidade_federacao',
    )
    list_filter = (
        'codigo_unidade_federacao',
        'nome_unidade_federacao',
        'sigla_unidade_federacao',
    )
    list_display = (
        'codigo_unidade_federacao',
        'nome_unidade_federacao',
        'sigla_unidade_federacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmUnidadesGestoras)
class TcmUnidadesGestorasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_unidade_gestora',
        'data_referencia',
        'nome_unidade_gestora',
        'data_criacao',
        'data_extincao',
        'numero_lei_criacao',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_unidade_gestora',
        'data_referencia',
        'nome_unidade_gestora',
        'data_criacao',
        'data_extincao',
        'numero_lei_criacao',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_municipio',
        'codigo_unidade_gestora',
        'data_referencia',
        'nome_unidade_gestora',
        'data_criacao',
        'data_extincao',
        'numero_lei_criacao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(TcmUnidadesOrcamentarias)
class TcmUnidadesOrcamentariasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_unidade',
        'tipo_administracao_unidade',
    )
    list_filter = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_unidade',
        'tipo_administracao_unidade',
    )
    list_display = (
        'exercicio_orcamento',
        'codigo_unidade',
        'codigo_municipio',
        'codigo_orgao',
        'codigo_tipo_unidade',
        'nome_unidade',
        'tipo_administracao_unidade',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecEmpenhos)
class AspecEmpenhosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'numero',
        'data',
        'tipo',
        'credor_nome',
        'credor_cnpj',
        'licitacao_modalidade',
        'licitacao_numero',
        'unidade_orcamentaria_codigo',
        'unidade_orcamentaria_titulo',
        'funcao_codigo',
        'funcao_titulo',
        'subfuncao_codigo',
        'subfuncao_titulo',
        'programa_codigo',
        'programa_titulo',
        'acao_codigo',
        'acao_titulo',
        'elemento_despesa_codigo',
        'elemento_despesa_titulo',
        'fonte',
        'historico',
    )
    list_filter = (
        'numero',
        'data',
        'tipo',
        'credor_nome',
        'credor_cnpj',
        'licitacao_modalidade',
        'licitacao_numero',
        'unidade_orcamentaria_codigo',
        'unidade_orcamentaria_titulo',
        'funcao_codigo',
        'funcao_titulo',
        'subfuncao_codigo',
        'subfuncao_titulo',
        'programa_codigo',
        'programa_titulo',
        'acao_codigo',
        'acao_titulo',
        'elemento_despesa_codigo',
        'elemento_despesa_titulo',
        'fonte',
        'historico',
    )
    list_display = (
        'numero',
        'data',
        'tipo',
        'credor_nome',
        'credor_cnpj',
        'licitacao_modalidade',
        'licitacao_numero',
        'unidade_orcamentaria_codigo',
        'unidade_orcamentaria_titulo',
        'funcao_codigo',
        'funcao_titulo',
        'subfuncao_codigo',
        'subfuncao_titulo',
        'programa_codigo',
        'programa_titulo',
        'acao_codigo',
        'acao_titulo',
        'elemento_despesa_codigo',
        'elemento_despesa_titulo',
        'fonte',
        'historico',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecEmpenhosMovimentos)
class AspecEmpenhosMovimentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'aspec_empenho',
        'documento',
        'data',
        'tipo',
        'registro',
        'valor',
    )
    list_filter = (
        'aspec_empenho',
        'documento',
        'data',
        'tipo',
        'registro',
        'valor',
    )
    list_display = (
        'aspec_empenho',
        'documento',
        'data',
        'tipo',
        'registro',
        'valor',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecLiquidacoes)
class AspecLiquidacoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'numero',
        'data',
        'valor',
        'nota_fiscal_numero',
        'nota_fiscal_serie',
        'nota_fiscal_tipo',
        'nota_fiscal_data',
    )
    list_filter = (
        'numero',
        'data',
        'valor',
        'nota_fiscal_numero',
        'nota_fiscal_serie',
        'nota_fiscal_tipo',
        'nota_fiscal_data',
    )
    list_display = (
        'numero',
        'data',
        'valor',
        'nota_fiscal_numero',
        'nota_fiscal_serie',
        'nota_fiscal_tipo',
        'nota_fiscal_data',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecLiquidacoesItens)
class AspecLiquidacoesItensAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'aspec_liquidacao',
        'descricao_item',
        'quantidade',
        'unidade',
        'valor_unitario',
        'valor_total',
    )
    list_filter = (
        'aspec_liquidacao',
        'descricao_item',
        'quantidade',
        'unidade',
        'valor_unitario',
        'valor_total',
    )
    list_display = (
        'aspec_liquidacao',
        'descricao_item',
        'quantidade',
        'unidade',
        'valor_unitario',
        'valor_total',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecPagamentos)
class AspecPagamentosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'numero',
        'data_liquidacao',
        'valor_total',
    )
    list_filter = (
        'numero',
        'data_liquidacao',
        'valor_total',
    )
    list_display = (
        'numero',
        'data_liquidacao',
        'valor_total',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(AspecPagamentosDetalhes)
class AspecPagamentosDetalhesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'aspec_pagamentos',
        'tipo',
        'forma',
        'valor',
        'documento_numero',
        'banco_nome',
        'agencia_nome',
        'agencia_numero',
        'conta_corrente_numero',
    )
    list_filter = (
        'aspec_pagamentos',
        'tipo',
        'forma',
        'valor',
        'documento_numero',
        'banco_nome',
        'agencia_nome',
        'agencia_numero',
        'conta_corrente_numero',
    )
    list_display = (
        'aspec_pagamentos',
        'tipo',
        'forma',
        'valor',
        'documento_numero',
        'banco_nome',
        'agencia_nome',
        'agencia_numero',
        'conta_corrente_numero',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]