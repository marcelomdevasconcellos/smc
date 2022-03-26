# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class TcmAgentesPublicos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_ingresso': 6, 
        'codigo_ocupacao_cbo': 6, 
        'codigo_amparo_legal': 6, 
        'codigo_expediente': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa_social': 6, 
        'codigo_regime_juridico': 6, 
        'codigo_regime_previdencia': 6, 
        'codigo_vinculo': 6, 
        'cpf_servidor': 6, 
        'data_posse': 6, 
        'data_publicacao_amparo_legal': 6, 
        'data_referencia_agente_publico': 6, 
        'data_amparo_legal': 6, 
        'data_expediente': 6, 
        'nome_servidor': 6, 
        'numero_matricula': 6, 
        'numero_dependentes': 6, 
        'numero_amparo_legal': 6, 
        'numero_expediente_nomeacao': 6, 
        'situacao_funcional': 6, 
        'tipo_cargo': 6, 
        'tipo_programa_social': 6, 
        'valor_carga_horaria': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_ingresso = models.CharField(
        'Código de Ingresso', 
        max_length=500, )
    codigo_ocupacao_cbo = models.CharField(
        'Código de Ocupação (CBO)', 
        max_length=500, )
    codigo_amparo_legal = models.CharField(
        'Código do Amparo Legal', 
        max_length=500, )
    codigo_expediente = models.CharField(
        'Código do Expediente', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa_social = models.CharField(
        'Código do Programa Social', 
        max_length=500, )
    codigo_regime_juridico = models.CharField(
        'Código do Regime Jurídico', 
        max_length=500, )
    codigo_regime_previdencia = models.CharField(
        'Código do Regime Previdenciário', 
        max_length=500, )
    codigo_vinculo = models.CharField(
        'Código do Vinculo', 
        max_length=500, )
    cpf_servidor = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_posse = models.CharField(
        'Data de Posse', 
        max_length=500, )
    data_publicacao_amparo_legal = models.CharField(
        'Data de Publicação do Amparo Legal', 
        max_length=500, )
    data_referencia_agente_publico = models.CharField(
        'Data de Referência do Agente Público', 
        max_length=500, )
    data_amparo_legal = models.CharField(
        'Data do Amparo Legal', 
        max_length=500, )
    data_expediente = models.CharField(
        'Data do Expediente', 
        max_length=500, )
    nome_servidor = models.CharField(
        'Nome do Servidor', 
        max_length=500, )
    numero_matricula = models.CharField(
        'Número da Matricula', 
        max_length=500, )
    numero_dependentes = models.CharField(
        'Número de Dependentes', 
        max_length=500, )
    numero_amparo_legal = models.CharField(
        'Número do Amparo Legal', 
        max_length=500, )
    numero_expediente_nomeacao = models.CharField(
        'Número do Expediente da Nomeação', 
        max_length=500, )
    situacao_funcional = models.CharField(
        'Situação Funcional', 
        max_length=500, )
    tipo_cargo = models.CharField(
        'Tipo de Cargo', 
        max_length=500, )
    tipo_programa_social = models.CharField(
        'Tipo de Programa Social', 
        max_length=500, )
    valor_carga_horaria = models.DecimalField(
        'Valor da Carga Horária',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_ingresso, self.codigo_ocupacao_cbo, self.codigo_amparo_legal, self.codigo_expediente, self.codigo_municipio, self.codigo_orgao, self.codigo_programa_social, self.codigo_regime_juridico, self.codigo_regime_previdencia, self.codigo_vinculo, self.cpf_servidor, self.data_posse, self.data_publicacao_amparo_legal, self.data_referencia_agente_publico, self.data_amparo_legal, self.data_expediente, self.nome_servidor, self.numero_matricula, self.numero_dependentes, self.numero_amparo_legal, self.numero_expediente_nomeacao, self.situacao_funcional, self.tipo_cargo, self.tipo_programa_social, self.valor_carga_horaria)

    class Meta:
        verbose_name = 'Agente Público'
        verbose_name_plural = 'Agentes Públicos'



class TcmAnulacoesEmpenhos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_anulacao': 6, 
        'data_emissao_empenho': 6, 
        'data_referencia_anulacao': 6, 
        'descricao_anulacao': 6, 
        'modalidade_anulacao': 6, 
        'numero_anulacao': 6, 
        'numero_empenho': 6, 
        'valor_anterior_saldo_dotacao': 6, 
        'valor_atual_saldo_dotacao': 6, 
        'valor_anulacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_anulacao = models.CharField(
        'Data de Anulação', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_referencia_anulacao = models.CharField(
        'Data de Referência da Anulação', 
        max_length=500, )
    descricao_anulacao = models.TextField(
        'Descrição da Anulação', )
    modalidade_anulacao = models.CharField(
        'Modalidade de Anulação', 
        max_length=500, )
    numero_anulacao = models.CharField(
        'Número da Anulação', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    valor_anterior_saldo_dotacao = models.DecimalField(
        'Valor Anterior do Saldo da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_atual_saldo_dotacao = models.DecimalField(
        'Valor Atual do Saldo da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacao = models.DecimalField(
        'Valor da Anulação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_anulacao, self.data_emissao_empenho, self.data_referencia_anulacao, self.descricao_anulacao, self.modalidade_anulacao, self.numero_anulacao, self.numero_empenho, self.valor_anterior_saldo_dotacao, self.valor_atual_saldo_dotacao, self.valor_anulacao)

    class Meta:
        verbose_name = 'Empenho (Anulação)'
        verbose_name_plural = 'Empenhos (Anulações)'



class TcmAnulacoesTaloesExtras(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_conta': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_anulacao': 6, 
        'data_referencia': 6, 
        'data_talao_receita': 6, 
        'historico_anulacao': 6, 
        'modalidade_anulacao': 6, 
        'numero_talao_receita': 6, 
        'valor_anulacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_conta = models.CharField(
        'Código da Conta', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_anulacao = models.CharField(
        'Data de Anulação', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_talao_receita = models.CharField(
        'Data do Talão da Receita', 
        max_length=500, )
    historico_anulacao = models.CharField(
        'Histórico da Anulação', 
        max_length=500, )
    modalidade_anulacao = models.CharField(
        'Modalidade de Anulação', 
        max_length=500, )
    numero_talao_receita = models.CharField(
        'Número do Talão da Receita', 
        max_length=500, )
    valor_anulacao = models.DecimalField(
        'Valor da Anulação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_conta, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_anulacao, self.data_referencia, self.data_talao_receita, self.historico_anulacao, self.modalidade_anulacao, self.numero_talao_receita, self.valor_anulacao)

    class Meta:
        verbose_name = 'Talão Extra (Anulação)'
        verbose_name_plural = 'Talões Extras (Anulações)'



class TcmAnulacoesTaloesReceitas(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_fonte': 6, 
        'codigo_rubrica': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_anulacao': 6, 
        'data_referencia': 6, 
        'data_talao_receita': 6, 
        'historico_anulacao': 6, 
        'md_anul_atr': 6, 
        'numero_talao_receita': 6, 
        'tipo_fonte': 6, 
        'valor_anulacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_rubrica = models.CharField(
        'Código da Rubrica', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_anulacao = models.CharField(
        'Data de Anulação', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_talao_receita = models.CharField(
        'Data do Talão da Receita', 
        max_length=500, )
    historico_anulacao = models.CharField(
        'Histórico da Anulação', 
        max_length=500, )
    md_anul_atr = models.CharField(
        'Modalidade de Anulação', 
        max_length=500, )
    numero_talao_receita = models.CharField(
        'Número do Talão da Receita', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_anulacao = models.DecimalField(
        'Valor da Anulação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_fonte, self.codigo_rubrica, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_anulacao, self.data_referencia, self.data_talao_receita, self.historico_anulacao, self.md_anul_atr, self.numero_talao_receita, self.tipo_fonte, self.valor_anulacao)

    class Meta:
        verbose_name = 'Talão de Receita (Anulação)'
        verbose_name_plural = 'Talões de Receitas (Anulações)'



class TcmBalanceteDespesaExtraOrcamentaria(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_conta_extraorcamentaria': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_referencia': 6, 
        'tipo_balancete': 6, 
        'valor_anulacao_no_mes': 6, 
        'valor_anulacao_ate_mes': 6, 
        'valor_pago_no_mes': 6, 
        'valor_pago_ate_mes': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_conta_extraorcamentaria = models.CharField(
        'Código da Conta Extra-Orçamentária', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    tipo_balancete = models.CharField(
        'Tipo de Balancete', 
        max_length=500, )
    valor_anulacao_no_mes = models.DecimalField(
        'Valor Anulado no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacao_ate_mes = models.DecimalField(
        'Valor Anulado até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_no_mes = models.DecimalField(
        'Valor Pago no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_ate_mes = models.DecimalField(
        'Valor Pago até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_conta_extraorcamentaria, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_referencia, self.tipo_balancete, self.valor_anulacao_no_mes, self.valor_anulacao_ate_mes, self.valor_pago_no_mes, self.valor_pago_ate_mes)

    class Meta:
        verbose_name = 'Balancete de Despesa Extra-Orçamentária'
        verbose_name_plural = 'Balancetes de Despesas Extra-Orçamentárias'



class TcmBalanceteDespesaOrcamentaria(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'data_referencia': 6, 
        'numero_projeto_atividade': 6, 
        'numero_subprojeto_atividade': 6, 
        'tipo_balancete': 6, 
        'tipo_fonte': 6, 
        'valor_nulacoes_dotacao_ate_mes': 6, 
        'valor_nulacoes_dotacao_no_mes': 6, 
        'valor_anulacoes_empenhos_ate_mes': 6, 
        'valor_anulacoes_empenhos_no_mes': 6, 
        'valor_estornos_liquidacao_no_mes': 6, 
        'valor_estornos_liquidacao_ate_mes': 6, 
        'valor_estornos_pagos_ate_mes': 6, 
        'valor_estornos_pagos_no_mes': 6, 
        'valor_saldo_dotacao': 6, 
        'valor_empenhado_pagar': 6, 
        'valor_empenhado_ate_mes': 6, 
        'valor_empenhado_no_mes': 6, 
        'valor_fixado_orcamento_bal_despesa': 6, 
        'valor_liquidado_ate_mes': 6, 
        'valor_liquidado_no_mes': 6, 
        'valor_pago_ate_mes': 6, 
        'valor_pago_no_mes': 6, 
        'valor_supl_ate_mes': 6, 
        'valor_supl_no_mes': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    tipo_balancete = models.CharField(
        'Tipo de Balancete', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_nulacoes_dotacao_ate_mes = models.DecimalField(
        'Valor Anulado na Dotação até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_nulacoes_dotacao_no_mes = models.DecimalField(
        'Valor Anulado na Dotação no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacoes_empenhos_ate_mes = models.DecimalField(
        'Valor das Anulações dos Empenhos até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacoes_empenhos_no_mes = models.DecimalField(
        'Valor das Anulações dos Empenhos no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_estornos_liquidacao_no_mes = models.DecimalField(
        'Valor do Estornos de Liquidação no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_estornos_liquidacao_ate_mes = models.DecimalField(
        'Valor do Estornos de Liquidação no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_estornos_pagos_ate_mes = models.DecimalField(
        'Valor do Estornos de Pagos até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_estornos_pagos_no_mes = models.DecimalField(
        'Valor do Estornos de Pagos no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_saldo_dotacao = models.DecimalField(
        'Valor do Saldo da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_pagar = models.DecimalField(
        'Valor Empenhado a Pagar',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_ate_mes = models.DecimalField(
        'Valor Empenhado até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_no_mes = models.DecimalField(
        'Valor Empenhado no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_fixado_orcamento_bal_despesa = models.DecimalField(
        'Valor Fixado no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_ate_mes = models.DecimalField(
        'Valor Liquidado até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_no_mes = models.DecimalField(
        'Valor Liquidado no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_ate_mes = models.DecimalField(
        'Valor Pago até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_no_mes = models.DecimalField(
        'Valor Pago no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_supl_ate_mes = models.DecimalField(
        'Valor Suplementado até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_supl_no_mes = models.DecimalField(
        'Valor Suplementado no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.data_referencia, self.numero_projeto_atividade, self.numero_subprojeto_atividade, self.tipo_balancete, self.tipo_fonte, self.valor_nulacoes_dotacao_ate_mes, self.valor_nulacoes_dotacao_no_mes, self.valor_anulacoes_empenhos_ate_mes, self.valor_anulacoes_empenhos_no_mes, self.valor_estornos_liquidacao_no_mes, self.valor_estornos_liquidacao_ate_mes, self.valor_estornos_pagos_ate_mes, self.valor_estornos_pagos_no_mes, self.valor_saldo_dotacao, self.valor_empenhado_pagar, self.valor_empenhado_ate_mes, self.valor_empenhado_no_mes, self.valor_fixado_orcamento_bal_despesa, self.valor_liquidado_ate_mes, self.valor_liquidado_no_mes, self.valor_pago_ate_mes, self.valor_pago_no_mes, self.valor_supl_ate_mes, self.valor_supl_no_mes)

    class Meta:
        verbose_name = 'Balancete de Despesa Orçamentária'
        verbose_name_plural = 'Balancetes de Despesas Orçamentárias'



class TcmBalanceteReceitaExtraOrcamentaria(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_conta_extraorcamentaria': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_referencia': 6, 
        'tipo_balancete': 6, 
        'valor_nulacoes_dotacao_ate_mes': 6, 
        'valor_arrecadacao_empenhos_no_mes': 6, 
        'valor_arrecadacao_dotacao_ate_mes': 6, 
        'valor_anulacoes_empenhos_no_mes': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_conta_extraorcamentaria = models.CharField(
        'Código da Conta Extra-Orçamentária', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    tipo_balancete = models.CharField(
        'Tipo de Balancete', 
        max_length=500, )
    valor_nulacoes_dotacao_ate_mes = models.DecimalField(
        'Valor Anulado na Dotação até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadacao_empenhos_no_mes = models.DecimalField(
        'Valor Arrecadado dos Empenhos no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadacao_dotacao_ate_mes = models.DecimalField(
        'Valor Arrecadado na Dotação até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacoes_empenhos_no_mes = models.DecimalField(
        'Valor das Anulações dos Empenhos no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_conta_extraorcamentaria, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_referencia, self.tipo_balancete, self.valor_nulacoes_dotacao_ate_mes, self.valor_arrecadacao_empenhos_no_mes, self.valor_arrecadacao_dotacao_ate_mes, self.valor_anulacoes_empenhos_no_mes)

    class Meta:
        verbose_name = 'Balancete de Receita Extra-Orçamentária'
        verbose_name_plural = 'Balancetes de Receitas Extra-Orçamentárias'



class TcmBalanceteReceitaOrcamentaria(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_fonte': 6, 
        'codigo_rubrica': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_referencia': 6, 
        'tipo_balancete': 6, 
        'tipo_fonte': 6, 
        'valor_arrecadacao_ate_mes': 6, 
        'valor_arrecadacao_no_mes': 6, 
        'valor_anulacoes_ate_mes': 6, 
        'valor_anulacoes_no_mes': 6, 
        'valor_previsto_orcamento': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_rubrica = models.CharField(
        'Código da Rubrica', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    tipo_balancete = models.CharField(
        'Tipo de Balancete', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_arrecadacao_ate_mes = models.DecimalField(
        'Valor Arrecadado até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadacao_no_mes = models.DecimalField(
        'Valor da Arrecadação no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacoes_ate_mes = models.DecimalField(
        'Valor das Anulações até o Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_anulacoes_no_mes = models.DecimalField(
        'Valor das Anulações no Mês Atual',  
        max_digits=15, 
        decimal_places=2, )
    valor_previsto_orcamento = models.DecimalField(
        'Valor Previsto no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_fonte, self.codigo_rubrica, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_referencia, self.tipo_balancete, self.tipo_fonte, self.valor_arrecadacao_ate_mes, self.valor_arrecadacao_no_mes, self.valor_anulacoes_ate_mes, self.valor_anulacoes_no_mes, self.valor_previsto_orcamento)

    class Meta:
        verbose_name = 'Balancete de Receita Orçamentária'
        verbose_name_plural = 'Balancetes de Receitas Orçamentárias'



class TcmBensMunicipios(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'data_aquisicao_bem': 6, 
        'data_referencia_bem': 6, 
        'descricao_bem1': 6, 
        'descricao_bem2': 6, 
        'numero_registro_bem': 6, 
        'status_baixado_bem': 6, 
        'tipo_classificacao_bem': 6, 
        'tipo_natureza_bem': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    data_aquisicao_bem = models.CharField(
        'Data de Aquisição do Bem', 
        max_length=500, )
    data_referencia_bem = models.CharField(
        'Data de Referência do Bem', 
        max_length=500, )
    descricao_bem1 = models.TextField(
        'Descrição do Bem', )
    descricao_bem2 = models.TextField(
        'Descrição do Bem', )
    numero_registro_bem = models.CharField(
        'Número do Registro do Bem', 
        max_length=500, )
    status_baixado_bem = models.CharField(
        'Status do Bem Baixado', 
        max_length=500, )
    tipo_classificacao_bem = models.CharField(
        'Tipo de Classificação do Bem', 
        max_length=500, )
    tipo_natureza_bem = models.CharField(
        'Tipo de Natureza do Bem', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.data_aquisicao_bem, self.data_referencia_bem, self.descricao_bem1, self.descricao_bem2, self.numero_registro_bem, self.status_baixado_bem, self.tipo_classificacao_bem, self.tipo_natureza_bem)

    class Meta:
        verbose_name = 'Bem do Município'
        verbose_name_plural = 'Bens do Município'



class TcmChequesNotasPagamentos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_cheque': 6, 
        'data_emissao_empenho': 6, 
        'data_referencia_cheque': 6, 
        'nome_negociante_ng': 6, 
        'numero_agencia': 6, 
        'numero_conta': 6, 
        'numero_pagamento': 6, 
        'numero_banco': 6, 
        'numero_cheque': 6, 
        'numero_doc_ng': 6, 
        'numero_empenho': 6, 
        'tipo_documento_bancario': 6, 
        'valor_cheque': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_cheque = models.CharField(
        'Data de Emissão do Cheque', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_referencia_cheque = models.CharField(
        'Data de Referência do Cheque', 
        max_length=500, )
    nome_negociante_ng = models.CharField(
        'Nome do Negociante', 
        max_length=500, )
    numero_agencia = models.CharField(
        'Número da Agência', 
        max_length=500, )
    numero_conta = models.CharField(
        'Número da Conta', 
        max_length=500, )
    numero_pagamento = models.CharField(
        'Número da Nota de Pagamento', 
        max_length=500, )
    numero_banco = models.CharField(
        'Número do Banco', 
        max_length=500, )
    numero_cheque = models.CharField(
        'Número do Cheque', 
        max_length=500, )
    numero_doc_ng = models.CharField(
        'Número do Documento', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    tipo_documento_bancario = models.CharField(
        'Tipo de Documento Bancário', 
        max_length=500, )
    valor_cheque = models.DecimalField(
        'Valor do Cheque',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_cheque, self.data_emissao_empenho, self.data_referencia_cheque, self.nome_negociante_ng, self.numero_agencia, self.numero_conta, self.numero_pagamento, self.numero_banco, self.numero_cheque, self.numero_doc_ng, self.numero_empenho, self.tipo_documento_bancario, self.valor_cheque)

    class Meta:
        verbose_name = 'Cheque Emitido'
        verbose_name_plural = 'Cheques Emitidos'



class TcmClassificacao(BaseModel):
    cols = {
        'nome_classificacao': 6, 
        'codigo_classificacao': 6, }
    
    nome_classificacao = models.CharField(
        'Classificação', 
        max_length=500, )
    codigo_classificacao = models.CharField(
        'Código da Classificação', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {}'.format(self.nome_classificacao, self.codigo_classificacao)

    class Meta:
        verbose_name = 'Classificações'
        verbose_name_plural = 'Classificação'



class TcmComissoesLicitacoes(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'cpf_gestor': 6, 
        'data_criacao_comissao': 6, 
        'data_extincao_comissao': 6, 
        'numero_comissao': 6, 
        'numero_portaria_criacao': 6, 
        'numero_portaria_extincao': 6, 
        'tipo_comissao': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    cpf_gestor = models.CharField(
        'CPF do Gestor', 
        max_length=500, )
    data_criacao_comissao = models.CharField(
        'Data de Criação da Comissão', 
        max_length=500, )
    data_extincao_comissao = models.CharField(
        'Data de Extinção da Comissão', 
        max_length=500, )
    numero_comissao = models.CharField(
        'Número da Comissão', 
        max_length=500, )
    numero_portaria_criacao = models.CharField(
        'Número da Portaria de Criação', 
        max_length=500, )
    numero_portaria_extincao = models.CharField(
        'Número da Portaria de Extinção', 
        max_length=500, )
    tipo_comissao = models.CharField(
        'Tipo de Comissão', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.cpf_gestor, self.data_criacao_comissao, self.data_extincao_comissao, self.numero_comissao, self.numero_portaria_criacao, self.numero_portaria_extincao, self.tipo_comissao)

    class Meta:
        verbose_name = 'Comissão de Licitação'
        verbose_name_plural = 'Comissões de Licitações'



class TcmContasBancarias(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_funcao': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_abertura': 6, 
        'data_referencia': 6, 
        'descricao_objetivo': 6, 
        'numero_agencia': 6, 
        'numero_conta': 6, 
        'numero_banco': 6, 
        'tipo_conta': 6, 
        'valor_saldo_abertura': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_abertura = models.CharField(
        'Data de Abertura', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    descricao_objetivo = models.TextField(
        'Descrição/Objetivo', )
    numero_agencia = models.CharField(
        'Número da Agência', 
        max_length=500, )
    numero_conta = models.CharField(
        'Número da Conta', 
        max_length=500, )
    numero_banco = models.CharField(
        'Número do Banco', 
        max_length=500, )
    tipo_conta = models.CharField(
        'Tipo de Conta', 
        max_length=500, )
    valor_saldo_abertura = models.DecimalField(
        'Valor do Saldo da Abertura',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_funcao, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_abertura, self.data_referencia, self.descricao_objetivo, self.numero_agencia, self.numero_conta, self.numero_banco, self.tipo_conta, self.valor_saldo_abertura)

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'



class TcmContasExtraOrcamentarias(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_conta_extra_orc': 6, 
        'codigo_municipio': 6, 
        'data_referencia_doc': 6, 
        'desc_conta_extra_orc': 6, 
        'vl_saldo_ini': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_conta_extra_orc = models.CharField(
        'Código da Conta Extra-Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    data_referencia_doc = models.CharField(
        'Data de Referência do Documento', 
        max_length=500, )
    desc_conta_extra_orc = models.CharField(
        'Desconto na Conta Extra-Orçamentária', 
        max_length=500, )
    vl_saldo_ini = models.DecimalField(
        'Valor do Saldo',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_conta_extra_orc, self.codigo_municipio, self.data_referencia_doc, self.desc_conta_extra_orc, self.vl_saldo_ini)

    class Meta:
        verbose_name = 'Conta Extra-Orçamentária'
        verbose_name_plural = 'Contas Extra-Orçamentárias'



class TcmContratados(BaseModel):
    cols = {
        'cep_negociante': 6, 
        'codigo_municipio': 6, 
        'codigo_tipo_negociante': 6, 
        'cpf_gestor': 6, 
        'data_contrato': 6, 
        'endereco_negociante': 6, 
        'nome_municipio_negociante': 6, 
        'nome_negociante': 6, 
        'numero_contrato': 6, 
        'numero_documento_negociante': 6, 
        'fone_negociante': 6, 
        'codigo_uf': 6, }
    
    cep_negociante = models.CharField(
        'CEP', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=500, )
    cpf_gestor = models.CharField(
        'CPF do Gestor', 
        max_length=500, )
    data_contrato = models.CharField(
        'Data do Contrato', 
        max_length=500, )
    endereco_negociante = models.CharField(
        'Endereço do Negociante', 
        max_length=500, )
    nome_municipio_negociante = models.CharField(
        'Nome do Município do Negociante', 
        max_length=500, )
    nome_negociante = models.CharField(
        'Nome do Negociante', 
        max_length=500, )
    numero_contrato = models.CharField(
        'Número do Contrato', 
        max_length=500, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=500, )
    fone_negociante = models.CharField(
        'Telefone do Negociante', 
        max_length=500, )
    codigo_uf = models.CharField(
        'UF', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.cep_negociante, self.codigo_municipio, self.codigo_tipo_negociante, self.cpf_gestor, self.data_contrato, self.endereco_negociante, self.nome_municipio_negociante, self.nome_negociante, self.numero_contrato, self.numero_documento_negociante, self.fone_negociante, self.codigo_uf)

    class Meta:
        verbose_name = 'Contratado'
        verbose_name_plural = 'Contratados'



class TcmContratos(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'cpf_gestor': 6, 
        'data_inicio_vigencia_contrato': 6, 
        'data_fim_vigencia_contrato': 6, 
        'data_contrato': 6, 
        'data_contrato_original': 6, 
        'descricao_objeto_contrato': 6, 
        'modalidade_contrato': 6, 
        'numero_contrato': 6, 
        'numero_contrato_original': 6, 
        'tipo_contrato': 6, 
        'valor_total_contrato': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    cpf_gestor = models.CharField(
        'CPF do Gestor', 
        max_length=500, )
    data_inicio_vigencia_contrato = models.CharField(
        'Data de Início da Vigência do Contrato', 
        max_length=500, )
    data_fim_vigencia_contrato = models.CharField(
        'Data de Término da Vigência Contratual', 
        max_length=500, )
    data_contrato = models.CharField(
        'Data do Contrato', 
        max_length=500, )
    data_contrato_original = models.CharField(
        'Data do Contrato Original', 
        max_length=500, )
    descricao_objeto_contrato = models.TextField(
        'Descrição do Objeto do Contrato', )
    modalidade_contrato = models.CharField(
        'Modalidade do Contrato', 
        max_length=500, )
    numero_contrato = models.CharField(
        'Número do Contrato', 
        max_length=500, )
    numero_contrato_original = models.CharField(
        'Número do Contrato Original', 
        max_length=500, )
    tipo_contrato = models.CharField(
        'Tipo de Contrato', 
        max_length=500, )
    valor_total_contrato = models.DecimalField(
        'Valor Total do Contrato',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.cpf_gestor, self.data_inicio_vigencia_contrato, self.data_fim_vigencia_contrato, self.data_contrato, self.data_contrato_original, self.descricao_objeto_contrato, self.modalidade_contrato, self.numero_contrato, self.numero_contrato_original, self.tipo_contrato, self.valor_total_contrato)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'



class TcmCpfCnpj(BaseModel):
    cols = {
        'codigo_cnpj_cpf': 6, 
        'nome': 6, }
    
    codigo_cnpj_cpf = models.CharField(
        'CNPJ_CPF', 
        max_length=500, )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo_cnpj_cpf, self.nome)

    class Meta:
        verbose_name = 'CPF/CNPJ'
        verbose_name_plural = 'CPF/CNPJ'



class TcmCreditosAdicionais(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte_recursos': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade_orcamentaria': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'cd_elemento_despesa': 6, 
        'data_abertura_credito': 6, 
        'data_referencia_doc': 6, 
        'numero_lei': 6, 
        'numero_decreto': 6, 
        'numero_projeto_atividade': 6, 
        'numero_sub_projeto_atividade': 6, 
        'numero_abertura_credito_dia': 6, 
        'tipo_abertura_credito': 6, 
        'tipo_fonte': 6, 
        'valor_credito_anulacao': 6, 
        'valor_credito_excesso': 6, 
        'valor_credito_operacao': 6, 
        'valor_credito_super': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte_recursos = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade_orcamentaria = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    cd_elemento_despesa = models.CharField(
        'Código Elemento de Despesa', 
        max_length=500, )
    data_abertura_credito = models.CharField(
        'Data de Abertura de Crédito', 
        max_length=500, )
    data_referencia_doc = models.CharField(
        'Data de Referência do Documento', 
        max_length=500, )
    numero_lei = models.CharField(
        'Número da Lei', 
        max_length=500, )
    numero_decreto = models.CharField(
        'Número do Decreto', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_sub_projeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    numero_abertura_credito_dia = models.CharField(
        'numero_abertura_credito_dia', 
        max_length=500, )
    tipo_abertura_credito = models.CharField(
        'Tipo da Abertura do Crédito', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_credito_anulacao = models.DecimalField(
        'Valor do Crédito (Anulação)',  
        max_digits=15, 
        decimal_places=2, )
    valor_credito_excesso = models.DecimalField(
        'Valor do Crédito (Excesso)',  
        max_digits=15, 
        decimal_places=2, )
    valor_credito_operacao = models.DecimalField(
        'Valor do Crédito (Operação)',  
        max_digits=15, 
        decimal_places=2, )
    valor_credito_super = models.DecimalField(
        'Valor do Crédito (Super)',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte_recursos, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade_orcamentaria, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.cd_elemento_despesa, self.data_abertura_credito, self.data_referencia_doc, self.numero_lei, self.numero_decreto, self.numero_projeto_atividade, self.numero_sub_projeto_atividade, self.numero_abertura_credito_dia, self.tipo_abertura_credito, self.tipo_fonte, self.valor_credito_anulacao, self.valor_credito_excesso, self.valor_credito_operacao, self.valor_credito_super)

    class Meta:
        verbose_name = 'Crédito Adicional'
        verbose_name_plural = 'Créditos Adicionais'



class TcmDadosOrcamentos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_municipio': 6, 
        'data_aprov_loa': 6, 
        'data_envio_loa': 6, 
        'data_public_loa': 6, 
        'nu_lei_orcamento': 6, 
        'numero_perc_sup_orcamento': 6, 
        'valor_total_fixado_orcamento': 6, 
        'valor_total_supl_orcamento': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    data_aprov_loa = models.CharField(
        'Data de Aprovação da LOA', 
        max_length=500, )
    data_envio_loa = models.CharField(
        'Data de Envio da LOA', 
        max_length=500, )
    data_public_loa = models.CharField(
        'Data de Publicação da LOA', 
        max_length=500, )
    nu_lei_orcamento = models.CharField(
        'Número da LOA', 
        max_length=500, )
    numero_perc_sup_orcamento = models.CharField(
        'Percentual de Suplementação do Orçamento', 
        max_length=500, )
    valor_total_fixado_orcamento = models.DecimalField(
        'Valor Total Fixado no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    valor_total_supl_orcamento = models.DecimalField(
        'Valor Total Suplementado no Orçamento',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_municipio, self.data_aprov_loa, self.data_envio_loa, self.data_public_loa, self.nu_lei_orcamento, self.numero_perc_sup_orcamento, self.valor_total_fixado_orcamento, self.valor_total_supl_orcamento)

    class Meta:
        verbose_name = 'Lei Orçamentária Anual'
        verbose_name_plural = 'Lei Orçamentária Anual'



class TcmDadosPessoais(BaseModel):
    cols = {
        'cpf_servidor': 6, 
        'data_nascimento_servidor': 6, 
        'nome_mae': 6, 
        'nome_pai': 6, 
        'nome_servidor': 6, 
        'nu_identidade': 6, }
    
    cpf_servidor = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_nascimento_servidor = models.CharField(
        'Data de Nascimento do Servidor', 
        max_length=500, )
    nome_mae = models.CharField(
        'Nome da Mãe', 
        max_length=500, )
    nome_pai = models.CharField(
        'Nome do Pai', 
        max_length=500, )
    nome_servidor = models.CharField(
        'Nome do Servidor', 
        max_length=500, )
    nu_identidade = models.CharField(
        'Número da Identidade', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.cpf_servidor, self.data_nascimento_servidor, self.nome_mae, self.nome_pai, self.nome_servidor, self.nu_identidade)

    class Meta:
        verbose_name = 'Dado Pessoal'
        verbose_name_plural = 'Dados Pessoais'



class TcmDespesaCategoriaEconomica(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'nome_elemento_despesa': 6, 
        'valor_total_fixado': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    nome_elemento_despesa = models.CharField(
        'Nome do Elemento de Despesa', 
        max_length=500, )
    valor_total_fixado = models.DecimalField(
        'Valor Total Fixado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.nome_elemento_despesa, self.valor_total_fixado)

    class Meta:
        verbose_name = 'Categoria Econômica'
        verbose_name_plural = 'Categorias Econômicas'



class TcmDespesaElementoProjeto(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'numero_projeto_atividade': 6, 
        'numero_subprojeto_atividade': 6, 
        'tipo_fonte': 6, 
        'valor_atual_categoria_economica': 6, 
        'valor_orcado_categoria_economica': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_atual_categoria_economica = models.DecimalField(
        'Valor Atual da Categoria Econômica',  
        max_digits=15, 
        decimal_places=2, )
    valor_orcado_categoria_economica = models.DecimalField(
        'Valor Orçado na Categoria Econômica',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.numero_projeto_atividade, self.numero_subprojeto_atividade, self.tipo_fonte, self.valor_atual_categoria_economica, self.valor_orcado_categoria_economica)

    class Meta:
        verbose_name = 'Elemento de Despesa'
        verbose_name_plural = 'Elementos de Despesa'



class TcmDespesaProjetoAtividade(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'codigo_tipo_orcamento': 6, 
        'descricao_projeto_atividade': 6, 
        'nome_projeto_atividade': 6, 
        'numero_projeto_atividade': 6, 
        'numero_subprojeto_atividade': 6, 
        'valor_total_fixado_projeto_atividade': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    codigo_tipo_orcamento = models.CharField(
        'Código do Tipo de Orçamento', 
        max_length=500, )
    descricao_projeto_atividade = models.TextField(
        'Descrição da Ação', )
    nome_projeto_atividade = models.CharField(
        'Nome da Ação', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    valor_total_fixado_projeto_atividade = models.DecimalField(
        'Valor Total Fixado no Projeto-Atividade',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.codigo_tipo_orcamento, self.descricao_projeto_atividade, self.nome_projeto_atividade, self.numero_projeto_atividade, self.numero_subprojeto_atividade, self.valor_total_fixado_projeto_atividade)

    class Meta:
        verbose_name = 'Projeto-Atividade (Ação)'
        verbose_name_plural = 'Projetos-Atividades (Ações)'



class TcmDespesasExtraOrcamentaria(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_conta_extraorcamentaria': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_despesa_extra': 6, 
        'data_referencia_documentacao': 6, 
        'nome_credor_despesa_extra': 6, 
        'numero_agencia': 6, 
        'numero_conta': 6, 
        'numero_banco': 6, 
        'numero_documento_caixa': 6, 
        'numero_documento_despesa_extra': 6, 
        'status_estorno_despesa_extra': 6, 
        'tipo_documento_despesa_extra': 6, 
        'valor_deducao_despesa_extra': 6, 
        'valor_documento_despesa_extra': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_conta_extraorcamentaria = models.CharField(
        'Código da Conta Extra-Orçamentária', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_despesa_extra = models.CharField(
        'Data de Emissão (Despesa Extra)', 
        max_length=500, )
    data_referencia_documentacao = models.CharField(
        'Data de Referência da Documentação', 
        max_length=500, )
    nome_credor_despesa_extra = models.CharField(
        'Nome do Credor da Despesa Extra', 
        max_length=500, )
    numero_agencia = models.CharField(
        'Número da Agência', 
        max_length=500, )
    numero_conta = models.CharField(
        'Número da Conta', 
        max_length=500, )
    numero_banco = models.CharField(
        'Número do Banco', 
        max_length=500, )
    numero_documento_caixa = models.CharField(
        'Número do Documento de Caixa', 
        max_length=500, )
    numero_documento_despesa_extra = models.CharField(
        'Número do Documento de Despesa Extra Orçamentária', 
        max_length=500, )
    status_estorno_despesa_extra = models.CharField(
        'Status do Estorno da Despesa Extra', 
        max_length=500, )
    tipo_documento_despesa_extra = models.CharField(
        'Tipo de Documento de Despesa Extra', 
        max_length=500, )
    valor_deducao_despesa_extra = models.DecimalField(
        'Valor de Dedução da Despesa Extra',  
        max_digits=15, 
        decimal_places=2, )
    valor_documento_despesa_extra = models.DecimalField(
        'Valor do Documento de Despesa Extra',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_conta_extraorcamentaria, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_despesa_extra, self.data_referencia_documentacao, self.nome_credor_despesa_extra, self.numero_agencia, self.numero_conta, self.numero_banco, self.numero_documento_caixa, self.numero_documento_despesa_extra, self.status_estorno_despesa_extra, self.tipo_documento_despesa_extra, self.valor_deducao_despesa_extra, self.valor_documento_despesa_extra)

    class Meta:
        verbose_name = 'Despesa Extra-Orçamentária'
        verbose_name_plural = 'Despesas Extra-Orçamentárias'



class TcmDestinoRealocacoesOrcamentarias(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'data_alteracao': 6, 
        'data_referencia': 6, 
        'numero_projeto_atividade': 6, 
        'numero_sub_projeto_atividade': 6, 
        'numero_sequencia': 6, 
        'tipo_fonte': 6, 
        'valor_destino': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    data_alteracao = models.CharField(
        'Data de Alteração', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_sub_projeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    numero_sequencia = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_destino = models.DecimalField(
        'Valor do Destino',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.data_alteracao, self.data_referencia, self.numero_projeto_atividade, self.numero_sub_projeto_atividade, self.numero_sequencia, self.tipo_fonte, self.valor_destino)

    class Meta:
        verbose_name = 'Destino de Realocação Orçamentária'
        verbose_name_plural = 'Destinos das Realocações Orçamentárias'



class TcmDotacoesLicitacoes(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'data_realizacao_licitacao': 6, 
        'numero_licitacao': 6, 
        'numero_projeto_atividade': 6, 
        'numero_subprojeto_atividade': 6, 
        'tipo_fonte': 6, 
        'valor_dotacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realizaçao da Licitação', 
        max_length=500, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_dotacao = models.DecimalField(
        'Valor da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.data_realizacao_licitacao, self.numero_licitacao, self.numero_projeto_atividade, self.numero_subprojeto_atividade, self.tipo_fonte, self.valor_dotacao)

    class Meta:
        verbose_name = 'Dotação da Licitação'
        verbose_name_plural = 'Dotações da Licitação'



class TcmEmpenhosBens(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_empenho': 6, 
        'data_referencia': 6, 
        'numero_nota_empenho': 6, 
        'numero_registro_bem': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    numero_nota_empenho = models.CharField(
        'Número da Nota de Empenho', 
        max_length=500, )
    numero_registro_bem = models.CharField(
        'Número do Registro do Bem', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_empenho, self.data_referencia, self.numero_nota_empenho, self.numero_registro_bem)

    class Meta:
        verbose_name = 'Bem do Empenho'
        verbose_name_plural = 'Bens do Empenho'



class TcmEstornosLiquidacoes(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_empenho': 6, 
        'data_estorno_liquidacao': 6, 
        'data_liquidacao': 6, 
        'data_referencia_estorno_liquidacao': 6, 
        'descricao_justificativa': 6, 
        'nome_assessor': 6, 
        'numero_empenho': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_estorno_liquidacao = models.CharField(
        'Data de Estorno da Liquidação', 
        max_length=500, )
    data_liquidacao = models.CharField(
        'Data de Liquidação', 
        max_length=500, )
    data_referencia_estorno_liquidacao = models.CharField(
        'Data de Referência do Estorno da Liquidação', 
        max_length=500, )
    descricao_justificativa = models.TextField(
        'Descrição/Justificativa', )
    nome_assessor = models.CharField(
        'Nome do Assessor', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_empenho, self.data_estorno_liquidacao, self.data_liquidacao, self.data_referencia_estorno_liquidacao, self.descricao_justificativa, self.nome_assessor, self.numero_empenho)

    class Meta:
        verbose_name = 'Estorno de Liquidação'
        verbose_name_plural = 'Estornos de Liquidações'



class TcmEstornosPagamentos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_empenho': 6, 
        'data_estorno_pagamento': 6, 
        'data_referencia_estorno_pagamento': 6, 
        'descricao_justificativa': 6, 
        'nome_assessor': 6, 
        'numero_pagamento': 6, 
        'numero_empenho': 6, 
        'numero_sub_empenho_nota_pagamento': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_estorno_pagamento = models.CharField(
        'Data de Estorno do Pagamento', 
        max_length=500, )
    data_referencia_estorno_pagamento = models.CharField(
        'Data de Referência do Estorno do Pagamento', 
        max_length=500, )
    descricao_justificativa = models.TextField(
        'Descrição/Justificativa', )
    nome_assessor = models.CharField(
        'Nome do Assessor', 
        max_length=500, )
    numero_pagamento = models.CharField(
        'Número da Nota de Pagamento', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_sub_empenho_nota_pagamento = models.CharField(
        'Número do Sub-Empenho', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_empenho, self.data_estorno_pagamento, self.data_referencia_estorno_pagamento, self.descricao_justificativa, self.nome_assessor, self.numero_pagamento, self.numero_empenho, self.numero_sub_empenho_nota_pagamento)

    class Meta:
        verbose_name = 'Estorno de Pagamentos'
        verbose_name_plural = 'Estornos de Pagamentos'



class TcmFontesAnulacao(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade_orcamentaria': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'data_abertura_credito': 6, 
        'numero_projeto_atividade': 6, 
        'numero_sub_projeto_atividade': 6, 
        'numero_abertura_credito_dia': 6, 
        'tipo_fonte': 6, 
        'valor_fonte_anul': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade_orcamentaria = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    data_abertura_credito = models.CharField(
        'Data de Abertura de Crédito', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_sub_projeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    numero_abertura_credito_dia = models.CharField(
        'numero_abertura_credito_dia', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_fonte_anul = models.DecimalField(
        'Valor Anulado na Fonte',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade_orcamentaria, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.data_abertura_credito, self.numero_projeto_atividade, self.numero_sub_projeto_atividade, self.numero_abertura_credito_dia, self.tipo_fonte, self.valor_fonte_anul)

    class Meta:
        verbose_name = 'Fonte de Anulação'
        verbose_name_plural = 'Fontes de Anulação'



class TcmFuncoes(BaseModel):
    cols = {
        'codigo_funcao': 6, 
        'nome_funcao': 6, }
    
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    nome_funcao = models.CharField(
        'Nome da Função', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo_funcao, self.nome_funcao)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'



class TcmGestores(BaseModel):
    cols = {
        'codigo': 6, 
        'nome': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=500, )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'



class TcmGestoresUnidadesGestoras(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade_gestora': 6, 
        'codigo_unidade': 6, 
        'codigo_ingresso': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_vinculo': 6, 
        'cpf_servidor': 6, 
        'data_inicio_gestao': 6, 
        'data_referencia': 6, 
        'data_fim_gestao': 6, 
        'nome_gestor': 6, 
        'numero_expediente': 6, 
        'status_ordenador_despesa': 6, 
        'tipo_cargo': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade_gestora = models.CharField(
        'Código da Unidade Gestora', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_ingresso = models.CharField(
        'Código de Ingresso', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_vinculo = models.CharField(
        'Código do Vinculo', 
        max_length=500, )
    cpf_servidor = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_inicio_gestao = models.CharField(
        'Data de Início da Gestão', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_fim_gestao = models.CharField(
        'Data de Término da Gestão', 
        max_length=500, )
    nome_gestor = models.CharField(
        'Nome do Gestor', 
        max_length=500, )
    numero_expediente = models.CharField(
        'Número do Expediente', 
        max_length=500, )
    status_ordenador_despesa = models.CharField(
        'Status do Ordenador de Despesa', 
        max_length=500, )
    tipo_cargo = models.CharField(
        'Tipo de Cargo', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade_gestora, self.codigo_unidade, self.codigo_ingresso, self.codigo_municipio, self.codigo_orgao, self.codigo_vinculo, self.cpf_servidor, self.data_inicio_gestao, self.data_referencia, self.data_fim_gestao, self.nome_gestor, self.numero_expediente, self.status_ordenador_despesa, self.tipo_cargo)

    class Meta:
        verbose_name = 'Gestor de Unidade Gestora'
        verbose_name_plural = 'Gestores de Unidades Gestoras'



class TcmGrupos(BaseModel):
    cols = {
        'codigo': 6, 
        'descricao': 6, 
        'nome': 6, 
        'ordem': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=500, )
    descricao = models.TextField(
        'Descrição', )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    ordem = models.CharField(
        'Ordem', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.codigo, self.descricao, self.nome, self.ordem)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'



class TcmItensLicitacoes(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'codigo_tipo_negociante': 6, 
        'data_realizacao_licitacao': 6, 
        'descricao_unidade_item_licitacao': 6, 
        'descricao_item_licitacao': 6, 
        'numero_licitacao': 6, 
        'numero_quantidade_item_licitacao': 6, 
        'numero_documento_negociante': 6, 
        'numero_sequencial_item_licitacao': 6, 
        'valor_unitario_item_licitacao': 6, 
        'valor_vencedor_item_licitacao': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realizaçao da Licitação', 
        max_length=500, )
    descricao_unidade_item_licitacao = models.TextField(
        'Descrição da Unidade do Item da Licitação', )
    descricao_item_licitacao = models.TextField(
        'Descrição do Item da Licitação', )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    numero_quantidade_item_licitacao = models.CharField(
        'Número da Quantidade do Item na Licitação', 
        max_length=500, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=500, )
    numero_sequencial_item_licitacao = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    valor_unitario_item_licitacao = models.DecimalField(
        'Valor Unitário do Item na Licitação',  
        max_digits=15, 
        decimal_places=2, )
    valor_vencedor_item_licitacao = models.DecimalField(
        'Valor Vencedor do Item na Licitação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.codigo_tipo_negociante, self.data_realizacao_licitacao, self.descricao_unidade_item_licitacao, self.descricao_item_licitacao, self.numero_licitacao, self.numero_quantidade_item_licitacao, self.numero_documento_negociante, self.numero_sequencial_item_licitacao, self.valor_unitario_item_licitacao, self.valor_vencedor_item_licitacao)

    class Meta:
        verbose_name = 'Item da Licitação'
        verbose_name_plural = 'Itens da Licitação'



class TcmItensNotasFiscais(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'exercicio_orcamento': 6, 
        'codigo_orgao': 6, 
        'codigo_unidade': 6, 
        'data_emissao': 6, 
        'numero_nota_empenho': 6, 
        'data_liquidacao': 6, 
        'tipo_nota_fiscal': 6, 
        'numero_nota_fiscal': 6, 
        'numero_item_sequencial': 6, 
        'descricao1_item': 6, 
        'descricao2_item': 6, 
        'unidade_compra': 6, 
        'numero_quantidade_comprada': 6, 
        'valor_unitario_item': 6, 
        'valor_total_item': 6, 
        'codigo_ncm': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    data_emissao = models.CharField(
        'Data de Emissão', 
        max_length=500, )
    numero_nota_empenho = models.CharField(
        'Número da Nota de Empenho', 
        max_length=500, )
    data_liquidacao = models.CharField(
        'Data de Liquidação', 
        max_length=500, )
    tipo_nota_fiscal = models.CharField(
        'Tipo de Nota Fiscal', 
        max_length=500, )
    numero_nota_fiscal = models.CharField(
        'Número da Nota Fiscal', 
        max_length=500, )
    numero_item_sequencial = models.CharField(
        'Número do Item', 
        max_length=500, )
    descricao1_item = models.TextField(
        'Descrição do Item', )
    descricao2_item = models.TextField(
        'Descrição do Item', )
    unidade_compra = models.CharField(
        'Unidade de Compra', 
        max_length=500, )
    numero_quantidade_comprada = models.CharField(
        'Número da Quantidade Comprada', 
        max_length=500, )
    valor_unitario_item = models.DecimalField(
        'Valor Unitário do Item',  
        max_digits=15, 
        decimal_places=2, )
    valor_total_item = models.DecimalField(
        'Valor Total do Item',  
        max_digits=15, 
        decimal_places=2, )
    codigo_ncm = models.CharField(
        'Código NCM (Nomenclatura Comum do Mercosul)', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.exercicio_orcamento, self.codigo_orgao, self.codigo_unidade, self.data_emissao, self.numero_nota_empenho, self.data_liquidacao, self.tipo_nota_fiscal, self.numero_nota_fiscal, self.numero_item_sequencial, self.descricao1_item, self.descricao2_item, self.unidade_compra, self.numero_quantidade_comprada, self.valor_unitario_item, self.valor_total_item, self.codigo_ncm)

    class Meta:
        verbose_name = 'Item da Nota-Fiscal'
        verbose_name_plural = 'Itens da Nota Fiscal'



class TcmItensRemuneratorios(BaseModel):
    cols = {
        'codigo_amparo_legal': 6, 
        'codigo_item': 6, 
        'codigo_municipio': 6, 
        'data_publicacao': 6, 
        'data_publicacao_decreto': 6, 
        'data_referencia': 6, 
        'data_amparo_legal': 6, 
        'data_decreto': 6, 
        'descricao_item': 6, 
        'numeto_amparo_legal': 6, 
        'numero_decreto': 6, 
        'st_extinto_ir': 6, 
        'tipo_classificacao': 6, 
        'tipo_item': 6, }
    
    codigo_amparo_legal = models.CharField(
        'Código do Amparo Legal', 
        max_length=500, )
    codigo_item = models.CharField(
        'Código do Item', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    data_publicacao = models.CharField(
        'Data de Publicação', 
        max_length=500, )
    data_publicacao_decreto = models.CharField(
        'Data de Publicação do Decreto', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_amparo_legal = models.CharField(
        'Data do Amparo Legal', 
        max_length=500, )
    data_decreto = models.CharField(
        'Data do Decreto', 
        max_length=500, )
    descricao_item = models.TextField(
        'Descrição do Item', )
    numeto_amparo_legal = models.CharField(
        'Número do Amparo Legal', 
        max_length=500, )
    numero_decreto = models.CharField(
        'Número do Decreto', 
        max_length=500, )
    st_extinto_ir = models.CharField(
        'st_extinto_ir', 
        max_length=500, )
    tipo_classificacao = models.CharField(
        'Tipo de Classificação', 
        max_length=500, )
    tipo_item = models.CharField(
        'Tipo de Item', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_amparo_legal, self.codigo_item, self.codigo_municipio, self.data_publicacao, self.data_publicacao_decreto, self.data_referencia, self.data_amparo_legal, self.data_decreto, self.descricao_item, self.numeto_amparo_legal, self.numero_decreto, self.st_extinto_ir, self.tipo_classificacao, self.tipo_item)

    class Meta:
        verbose_name = 'Item Remuneratório'
        verbose_name_plural = 'Itens Remuneratórios'



class TcmLicitacoes(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'cpf_gestor': 6, 
        'cpf_responsavel_juridico': 6, 
        'cpf_responsavel_homologacao': 6, 
        'data_criacao_comissao': 6, 
        'data_emissao_edital': 6, 
        'data_homologacao': 6, 
        'data_realizacao_autuacao_licitacao': 6, 
        'data_realizacao_licitacao': 6, 
        'descricao1_motivo_fornecedor': 6, 
        'descricao2_motivo_fornecedor': 6, 
        'descricao1_objeto_licitacao': 6, 
        'descricao2_objeto_licitacao': 6, 
        'descricao1_justificativa_preco': 6, 
        'descricao2_justificativa_preco': 6, 
        'hora_licitacao': 6, 
        'modalidade_licitacao': 6, 
        'modalidade_processo_administrativo': 6, 
        'nome_orgao_ata': 6, 
        'nome_responsavel_juridico': 6, 
        'nome_responsavel_homologacao': 6, 
        'numero_comissao': 6, 
        'numero_licitacao': 6, 
        'tipo_licitacao': 6, 
        'valor_limite_superior': 6, 
        'valor_orcado_estimado': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    cpf_gestor = models.CharField(
        'CPF do Gestor', 
        max_length=500, )
    cpf_responsavel_juridico = models.CharField(
        'CPF do Responsável Jurídico', 
        max_length=500, )
    cpf_responsavel_homologacao = models.CharField(
        'CPF do Responsável pela Homologação', 
        max_length=500, )
    data_criacao_comissao = models.CharField(
        'Data de Criação da Comissão', 
        max_length=500, )
    data_emissao_edital = models.CharField(
        'Data de Emissão do Edital', 
        max_length=500, )
    data_homologacao = models.CharField(
        'Data de Homologação', 
        max_length=500, )
    data_realizacao_autuacao_licitacao = models.CharField(
        'Data de Realização da Autuação da Licitação', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realizaçao da Licitação', 
        max_length=500, )
    descricao1_motivo_fornecedor = models.TextField(
        'Descrição do Motivo do Fornecedor', )
    descricao2_motivo_fornecedor = models.TextField(
        'Descrição do Motivo do Fornecedor', )
    descricao1_objeto_licitacao = models.TextField(
        'Descrição do Objeto da Licitação', )
    descricao2_objeto_licitacao = models.TextField(
        'Descrição do Objeto da Licitação', )
    descricao1_justificativa_preco = models.TextField(
        'Descrição/Justificativa de Preço', )
    descricao2_justificativa_preco = models.TextField(
        'Descrição/Justificativa de Preço', )
    hora_licitacao = models.CharField(
        'Hora da Licitação', 
        max_length=500, )
    modalidade_licitacao = models.CharField(
        'Modalidade da Licitação', 
        max_length=500, )
    modalidade_processo_administrativo = models.CharField(
        'Modalidade do Processo Administrativo', 
        max_length=500, )
    nome_orgao_ata = models.CharField(
        'Nome do Órgão', 
        max_length=500, )
    nome_responsavel_juridico = models.CharField(
        'Nome do Responsável Jurídico', 
        max_length=500, )
    nome_responsavel_homologacao = models.CharField(
        'Nome do Responsável pela Homologação', 
        max_length=500, )
    numero_comissao = models.CharField(
        'Número da Comissão', 
        max_length=500, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    tipo_licitacao = models.CharField(
        'Tipo de Licitação', 
        max_length=500, )
    valor_limite_superior = models.DecimalField(
        'Valor do Limite Superior',  
        max_digits=15, 
        decimal_places=2, )
    valor_orcado_estimado = models.DecimalField(
        'Valor Orçado Estimado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.cpf_gestor, self.cpf_responsavel_juridico, self.cpf_responsavel_homologacao, self.data_criacao_comissao, self.data_emissao_edital, self.data_homologacao, self.data_realizacao_autuacao_licitacao, self.data_realizacao_licitacao, self.descricao1_motivo_fornecedor, self.descricao2_motivo_fornecedor, self.descricao1_objeto_licitacao, self.descricao2_objeto_licitacao, self.descricao1_justificativa_preco, self.descricao2_justificativa_preco, self.hora_licitacao, self.modalidade_licitacao, self.modalidade_processo_administrativo, self.nome_orgao_ata, self.nome_responsavel_juridico, self.nome_responsavel_homologacao, self.numero_comissao, self.numero_licitacao, self.tipo_licitacao, self.valor_limite_superior, self.valor_orcado_estimado)

    class Meta:
        verbose_name = 'Licitação'
        verbose_name_plural = 'Licitações'



class TcmLicitantes(BaseModel):
    cols = {
        'cep_negociante': 6, 
        'codigo_municipio': 6, 
        'codigo_tipo_negociante': 6, 
        'data_realizacao_licitacao': 6, 
        'endereco_negociante': 6, 
        'nome_municipio_negociante': 6, 
        'nome_negociante': 6, 
        'numero_licitacao': 6, 
        'numero_documento_negociante': 6, 
        'fone_negociante': 6, 
        'codigo_uf': 6, }
    
    cep_negociante = models.CharField(
        'CEP', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realizaçao da Licitação', 
        max_length=500, )
    endereco_negociante = models.CharField(
        'Endereço do Negociante', 
        max_length=500, )
    nome_municipio_negociante = models.CharField(
        'Nome do Município do Negociante', 
        max_length=500, )
    nome_negociante = models.CharField(
        'Nome do Negociante', 
        max_length=500, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=500, )
    fone_negociante = models.CharField(
        'Telefone do Negociante', 
        max_length=500, )
    codigo_uf = models.CharField(
        'UF', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.cep_negociante, self.codigo_municipio, self.codigo_tipo_negociante, self.data_realizacao_licitacao, self.endereco_negociante, self.nome_municipio_negociante, self.nome_negociante, self.numero_licitacao, self.numero_documento_negociante, self.fone_negociante, self.codigo_uf)

    class Meta:
        verbose_name = 'Licitante'
        verbose_name_plural = 'Licitantes'



class TcmLiquidacoes(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'cpf_responsavel_liquidacao': 6, 
        'data_emissao_empenho': 6, 
        'data_liquidacao': 6, 
        'data_referencia_liquidacao': 6, 
        'estado_folha': 6, 
        'estado_de_estorno': 6, 
        'nome_responsavel_liquidacao': 6, 
        'numero_empenho': 6, 
        'numero_sub_empenho_liquidacao': 6, 
        'valor_liquidado': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    cpf_responsavel_liquidacao = models.CharField(
        'CPF do Responsável pela Liquidação', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_liquidacao = models.CharField(
        'Data de Liquidação', 
        max_length=500, )
    data_referencia_liquidacao = models.CharField(
        'Data de Referência da Liquidação', 
        max_length=500, )
    estado_folha = models.CharField(
        'Estado da Folha', 
        max_length=500, )
    estado_de_estorno = models.CharField(
        'Estado de Estorno', 
        max_length=500, )
    nome_responsavel_liquidacao = models.CharField(
        'Nome do Responsável pela Liquidação', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_sub_empenho_liquidacao = models.CharField(
        'Número do Sub-Empenho', 
        max_length=500, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.cpf_responsavel_liquidacao, self.data_emissao_empenho, self.data_liquidacao, self.data_referencia_liquidacao, self.estado_folha, self.estado_de_estorno, self.nome_responsavel_liquidacao, self.numero_empenho, self.numero_sub_empenho_liquidacao, self.valor_liquidado)

    class Meta:
        verbose_name = 'Liquidação'
        verbose_name_plural = 'Liquidações'



class TcmMetodos(BaseModel):
    cols = {
        'codigo': 6, 
        'conexao': 6, 
        'descricao': 6, 
        'grupo': 6, 
        'nome': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=500, )
    conexao = models.CharField(
        'Conexão', 
        max_length=500, )
    descricao = models.TextField(
        'Descrição', )
    grupo = models.CharField(
        'Grupo', 
        max_length=500, )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.codigo, self.conexao, self.descricao, self.grupo, self.nome)

    class Meta:
        verbose_name = 'Método'
        verbose_name_plural = 'Métodos'



class TcmMovimentacoesFontes(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'exercicio_orcamento': 6, 
        'data_modificacao_fonte': 6, 
        'numero_modificacao_dia': 6, 
        'tipo_movimentacao': 6, 
        'codigo_orgao': 6, 
        'codigo_unidade': 6, 
        'funcao': 6, 
        'sub_funcao': 6, 
        'projeto_atividade': 6, 
        'numero_projeto_atividade': 6, 
        'numero_sub_projeto_atividade': 6, 
        'codigo_elemento_despesa': 6, 
        'grupo_fonte_origem': 6, 
        'codigo_fonte_origem': 6, 
        'grupo_fonte_destino': 6, 
        'codigo_fonte_destino': 6, 
        'valor_movimentacao_fonte': 6, 
        'data_referencia_movimentacao': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    data_modificacao_fonte = models.CharField(
        'Data de Modificação da Fonte', 
        max_length=500, )
    numero_modificacao_dia = models.CharField(
        'Número de Modificação Dia', 
        max_length=500, )
    tipo_movimentacao = models.CharField(
        'Tipo de Movimentação', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade', 
        max_length=500, )
    funcao = models.CharField(
        'Função', 
        max_length=500, )
    sub_funcao = models.CharField(
        'Sub-Função', 
        max_length=500, )
    projeto_atividade = models.CharField(
        'Projeto-Atividade', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_sub_projeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    grupo_fonte_origem = models.CharField(
        'Grupo de Fonte (Origem)', 
        max_length=500, )
    codigo_fonte_origem = models.CharField(
        'Código da Fonte (Origem)', 
        max_length=500, )
    grupo_fonte_destino = models.CharField(
        'Grupo de Fonte (Destino)', 
        max_length=500, )
    codigo_fonte_destino = models.CharField(
        'Código da Fonte (Destino)', 
        max_length=500, )
    valor_movimentacao_fonte = models.DecimalField(
        'Valor da Movimentação da Fonte',  
        max_digits=15, 
        decimal_places=2, )
    data_referencia_movimentacao = models.CharField(
        'Data de Referência da Movimentação', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.codigo_municipio, self.exercicio_orcamento, self.data_modificacao_fonte, self.numero_modificacao_dia, self.tipo_movimentacao, self.codigo_orgao, self.codigo_unidade, self.funcao, self.sub_funcao, self.projeto_atividade, self.numero_projeto_atividade, self.numero_sub_projeto_atividade, self.codigo_elemento_despesa, self.grupo_fonte_origem, self.codigo_fonte_origem, self.grupo_fonte_destino, self.codigo_fonte_destino, self.valor_movimentacao_fonte, self.data_referencia_movimentacao)

    class Meta:
        verbose_name = 'Movimentação Fonte'
        verbose_name_plural = 'Movimentações Fontes'



class TcmMunicipios(BaseModel):
    cols = {
        'codigo_municipio': 6, 
        'geoibgeid': 6, 
        'geonamesid': 6, 
        'nome_municipio': 6, }
    
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    geoibgeid = models.CharField(
        'GEO IBGE ID', 
        max_length=500, )
    geonamesid = models.CharField(
        'GEO NAMES ID', 
        max_length=500, )
    nome_municipio = models.CharField(
        'Nome do Município', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.codigo_municipio, self.geoibgeid, self.geonamesid, self.nome_municipio)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municípios'



class TcmNegociantes(BaseModel):
    cols = {
        'cep_negociante': 6, 
        'codigo_tipo_negociante': 6, 
        'endereco_negociante': 6, 
        'nome_municipio_negociante': 6, 
        'nome_negociante': 6, 
        'numero_documento_negociante': 6, 
        'fone_negociante': 6, 
        'uf_negociante': 6, }
    
    cep_negociante = models.CharField(
        'CEP', 
        max_length=500, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=500, )
    endereco_negociante = models.CharField(
        'Endereço do Negociante', 
        max_length=500, )
    nome_municipio_negociante = models.CharField(
        'Nome do Município do Negociante', 
        max_length=500, )
    nome_negociante = models.CharField(
        'Nome do Negociante', 
        max_length=500, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=500, )
    fone_negociante = models.CharField(
        'Telefone do Negociante', 
        max_length=500, )
    uf_negociante = models.CharField(
        'UF do Negociante', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.cep_negociante, self.codigo_tipo_negociante, self.endereco_negociante, self.nome_municipio_negociante, self.nome_negociante, self.numero_documento_negociante, self.fone_negociante, self.uf_negociante)

    class Meta:
        verbose_name = 'Negociante'
        verbose_name_plural = 'Negociantes'



class TcmNotasEmpenhos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'cep_negociante': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento_despesa': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'codigo_tipo_negociante': 6, 
        'cpf_gestor_contrato': 6, 
        'cd_cpf_gestor': 6, 
        'data_emissao_empenho': 6, 
        'data_emissao_empenho_substituto': 6, 
        'data_realizacao_licitacao': 6, 
        'data_referencia_empenho': 6, 
        'data_contrato': 6, 
        'descricao_empenho': 6, 
        'endereco_negociante': 6, 
        'estado_empenho': 6, 
        'modalidade_empenho': 6, 
        'nome_municipio_negociante': 6, 
        'nome_negociante': 6, 
        'numero_licitacao': 6, 
        'numero_nota_anulacao': 6, 
        'numero_contrato': 6, 
        'numero_documento_negociante': 6, 
        'numero_empenho': 6, 
        'numero_empenho_substituto': 6, 
        'numero_projeto_atividade': 6, 
        'numero_subprojeto_atividade': 6, 
        'fone_negociante': 6, 
        'tipo_fonte': 6, 
        'tipo_processo_licitatorio': 6, 
        'codigo_uf': 6, 
        'valor_anterior_saldo_dotacao': 6, 
        'valor_atual_saldo_dotacao': 6, 
        'valor_empenhado': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    cep_negociante = models.CharField(
        'CEP', 
        max_length=500, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=500, )
    cpf_gestor_contrato = models.CharField(
        'CPF do Gestor do Contrato', 
        max_length=500, )
    cd_cpf_gestor = models.CharField(
        'CPF Gestor', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_emissao_empenho_substituto = models.CharField(
        'Data de Emissão do Empenho Substituto', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realização da Licitação', 
        max_length=500, )
    data_referencia_empenho = models.CharField(
        'Data de Referência do Empenho', 
        max_length=500, )
    data_contrato = models.CharField(
        'Data do Contrato', 
        max_length=500, )
    descricao_empenho = models.TextField(
        'Descrição do Empenho', )
    endereco_negociante = models.CharField(
        'Endereço do Negociante', 
        max_length=500, )
    estado_empenho = models.CharField(
        'Estado do Empenho', 
        max_length=500, )
    modalidade_empenho = models.CharField(
        'Modalidade do Empenho', 
        max_length=500, )
    nome_municipio_negociante = models.CharField(
        'Nome do Município do Negociante', 
        max_length=500, )
    nome_negociante = models.CharField(
        'Nome do Negociante', 
        max_length=500, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    numero_nota_anulacao = models.CharField(
        'Número da Nota de Anulação', 
        max_length=500, )
    numero_contrato = models.CharField(
        'Número do Contrato', 
        max_length=500, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_empenho_substituto = models.CharField(
        'Número do Empenho Substituto', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    fone_negociante = models.CharField(
        'Telefone do Negociante', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    tipo_processo_licitatorio = models.CharField(
        'Tipo do Processo Licitatório', 
        max_length=500, )
    codigo_uf = models.CharField(
        'UF', 
        max_length=500, )
    valor_anterior_saldo_dotacao = models.DecimalField(
        'Valor Anterior do Saldo da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_atual_saldo_dotacao = models.DecimalField(
        'Valor Atual do Saldo da Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado = models.DecimalField(
        'Valor Empenhado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.cep_negociante, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento_despesa, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.codigo_tipo_negociante, self.cpf_gestor_contrato, self.cd_cpf_gestor, self.data_emissao_empenho, self.data_emissao_empenho_substituto, self.data_realizacao_licitacao, self.data_referencia_empenho, self.data_contrato, self.descricao_empenho, self.endereco_negociante, self.estado_empenho, self.modalidade_empenho, self.nome_municipio_negociante, self.nome_negociante, self.numero_licitacao, self.numero_nota_anulacao, self.numero_contrato, self.numero_documento_negociante, self.numero_empenho, self.numero_empenho_substituto, self.numero_projeto_atividade, self.numero_subprojeto_atividade, self.fone_negociante, self.tipo_fonte, self.tipo_processo_licitatorio, self.codigo_uf, self.valor_anterior_saldo_dotacao, self.valor_atual_saldo_dotacao, self.valor_empenhado)

    class Meta:
        verbose_name = 'Empenho'
        verbose_name_plural = 'Notas de Empenho'



class TcmNotasFiscais(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'cgf_emitente': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao': 6, 
        'data_emissao_empenho': 6, 
        'data_liquidacao': 6, 
        'data_referencia': 6, 
        'data_limite': 6, 
        'numero_nota_fiscal': 6, 
        'numero_serie': 6, 
        'numero_serie_selo_transito': 6, 
        'numero_empenho': 6, 
        'numero_formulario': 6, 
        'numero_protocolo_autenticacao': 6, 
        'numero_selo_transito': 6, 
        'tipo_emissao': 6, 
        'tipo_nota_fiscal': 6, 
        'valor_bruto': 6, 
        'valor_aliquota_iss': 6, 
        'valor_base_calculo_iss': 6, 
        'valor_desconto': 6, 
        'valor_liquido': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    cgf_emitente = models.CharField(
        'CNPJ', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao = models.CharField(
        'Data de Emissão', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_liquidacao = models.CharField(
        'Data de Liquidação', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_limite = models.CharField(
        'Data do Limite', 
        max_length=500, )
    numero_nota_fiscal = models.CharField(
        'Número da Nota Fiscal', 
        max_length=500, )
    numero_serie = models.CharField(
        'Número de Série', 
        max_length=500, )
    numero_serie_selo_transito = models.CharField(
        'Número de Série do Selo do Trânsito', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_formulario = models.CharField(
        'Número do Formulário', 
        max_length=500, )
    numero_protocolo_autenticacao = models.CharField(
        'Número do Protocolo de Autenticação', 
        max_length=500, )
    numero_selo_transito = models.CharField(
        'Número do Selo do Trânsito', 
        max_length=500, )
    tipo_emissao = models.CharField(
        'Tipo de Emissão', 
        max_length=500, )
    tipo_nota_fiscal = models.CharField(
        'Tipo de Nota Fiscal', 
        max_length=500, )
    valor_bruto = models.DecimalField(
        'Valor Bruto',  
        max_digits=15, 
        decimal_places=2, )
    valor_aliquota_iss = models.DecimalField(
        'Valor da Alíquota do ISS',  
        max_digits=15, 
        decimal_places=2, )
    valor_base_calculo_iss = models.DecimalField(
        'Valor de Base para Cálculo do ISS',  
        max_digits=15, 
        decimal_places=2, )
    valor_desconto = models.DecimalField(
        'Valor do Desconto',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquido = models.DecimalField(
        'Valor Líquido',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.cgf_emitente, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao, self.data_emissao_empenho, self.data_liquidacao, self.data_referencia, self.data_limite, self.numero_nota_fiscal, self.numero_serie, self.numero_serie_selo_transito, self.numero_empenho, self.numero_formulario, self.numero_protocolo_autenticacao, self.numero_selo_transito, self.tipo_emissao, self.tipo_nota_fiscal, self.valor_bruto, self.valor_aliquota_iss, self.valor_base_calculo_iss, self.valor_desconto, self.valor_liquido)

    class Meta:
        verbose_name = 'Nota-Fiscal'
        verbose_name_plural = 'Notas Fiscais'



class TcmNotasFiscaisLiquid(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'numero_cgf_emitente_nota_fiscal': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_emissao_nota_fiscal': 6, 
        'data_emissao_empenho': 6, 
        'data_liquidacao_nota_fiscal': 6, 
        'data_referencia_nota_fiscal': 6, 
        'data_limite_nota_fiscal': 6, 
        'nome_resp_liquidacao_nota_fiscal': 6, 
        'numero_nota_fiscal': 6, 
        'numero_serie_nota_fiscal': 6, 
        'numero_serie_transito_nota_fiscal': 6, 
        'numero_empenho': 6, 
        'numero_formulario_nota_fiscal': 6, 
        'numero_selo_transito_nota_fiscal': 6, 
        'numero_sub_empenho_nota_fiscal': 6, 
        'tipo_nota_fiscal': 6, 
        'uf_emitente_nota_fiscal': 6, 
        'valor_nota_fiscal': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    numero_cgf_emitente_nota_fiscal = models.CharField(
        'CNPJ do Emissor da Nota Fiscal', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_emissao_nota_fiscal = models.CharField(
        'Data de Emissão da Nota Fiscal', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_liquidacao_nota_fiscal = models.CharField(
        'Data de Liquidação da Nota Fiscal', 
        max_length=500, )
    data_referencia_nota_fiscal = models.CharField(
        'Data de Referência da Nota Fiscal', 
        max_length=500, )
    data_limite_nota_fiscal = models.CharField(
        'Data do Limite na Nota Fiscal', 
        max_length=500, )
    nome_resp_liquidacao_nota_fiscal = models.CharField(
        'Nome do Responsável pela Liquidação da Nota Fiscal', 
        max_length=500, )
    numero_nota_fiscal = models.CharField(
        'Número da Nota Fiscal', 
        max_length=500, )
    numero_serie_nota_fiscal = models.CharField(
        'Número de Série da Nota Fiscal', 
        max_length=500, )
    numero_serie_transito_nota_fiscal = models.CharField(
        'Número de Série do Trânsito na Nota Fiscal', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_formulario_nota_fiscal = models.CharField(
        'Número do Formulário da Nota Fiscal', 
        max_length=500, )
    numero_selo_transito_nota_fiscal = models.CharField(
        'Número do Selo do Trânsito', 
        max_length=500, )
    numero_sub_empenho_nota_fiscal = models.CharField(
        'Número do Sub-Empenho', 
        max_length=500, )
    tipo_nota_fiscal = models.CharField(
        'Tipo de Nota Fiscal', 
        max_length=500, )
    uf_emitente_nota_fiscal = models.CharField(
        'UF do Emitente na Nota Fiscal', 
        max_length=500, )
    valor_nota_fiscal = models.DecimalField(
        'Valor da Nota-Fiscal',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.numero_cgf_emitente_nota_fiscal, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_emissao_nota_fiscal, self.data_emissao_empenho, self.data_liquidacao_nota_fiscal, self.data_referencia_nota_fiscal, self.data_limite_nota_fiscal, self.nome_resp_liquidacao_nota_fiscal, self.numero_nota_fiscal, self.numero_serie_nota_fiscal, self.numero_serie_transito_nota_fiscal, self.numero_empenho, self.numero_formulario_nota_fiscal, self.numero_selo_transito_nota_fiscal, self.numero_sub_empenho_nota_fiscal, self.tipo_nota_fiscal, self.uf_emitente_nota_fiscal, self.valor_nota_fiscal)

    class Meta:
        verbose_name = 'Nota-Fiscal Liquidada'
        verbose_name_plural = 'Notas Fiscais Liquidadas'



class TcmNotasPagamentos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'cpf_pagador': 6, 
        'data_nota_pagamento': 6, 
        'data_emissao_empenho': 6, 
        'data_referencia': 6, 
        'estado_de_estornado': 6, 
        'nome_pagador': 6, 
        'numero_nota_pagamento': 6, 
        'nu_documento_caixa': 6, 
        'numero_empenho': 6, 
        'numero_sub_empenho': 6, 
        'valor_nota_pagamento': 6, 
        'valor_empenhado_a_pagar': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    cpf_pagador = models.CharField(
        'CPF do Pagador', 
        max_length=500, )
    data_nota_pagamento = models.CharField(
        'Data da Nota de Pagamento', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    estado_de_estornado = models.CharField(
        'Estado de Estornado', 
        max_length=500, )
    nome_pagador = models.CharField(
        'Nome do Pagador', 
        max_length=500, )
    numero_nota_pagamento = models.CharField(
        'Número da Nota de Pagamento', 
        max_length=500, )
    nu_documento_caixa = models.CharField(
        'Número do Documento de Caixa', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_sub_empenho = models.CharField(
        'Número do Sub-Empenho', 
        max_length=500, )
    valor_nota_pagamento = models.DecimalField(
        'Valor da Nota de Pagamento',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_a_pagar = models.DecimalField(
        'Valor Empenhado a Pagar',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.cpf_pagador, self.data_nota_pagamento, self.data_emissao_empenho, self.data_referencia, self.estado_de_estornado, self.nome_pagador, self.numero_nota_pagamento, self.nu_documento_caixa, self.numero_empenho, self.numero_sub_empenho, self.valor_nota_pagamento, self.valor_empenhado_a_pagar)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Notas de Pagamento'



class TcmOrcamentoReceita(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_fonte': 6, 
        'codigo_rubrica': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'descricao_rubrica': 6, 
        'tipo_fonte': 6, 
        'valor_previsto': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_rubrica = models.CharField(
        'Código da Rubrica', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    descricao_rubrica = models.TextField(
        'Descrição da Rubrica', )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_previsto = models.DecimalField(
        'Valor Previsto',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_fonte, self.codigo_rubrica, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.descricao_rubrica, self.tipo_fonte, self.valor_previsto)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'



class TcmOrdenadores(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade_gestora': 6, 
        'codigo_unidade': 6, 
        'codigo_ingresso': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_vinculo': 6, 
        'cpf_servidor': 6, 
        'data_inclusao_unidade_orcamentaria': 6, 
        'data_inicio_gestao_ordenador': 6, 
        'data_referencia_ordenador': 6, 
        'data_fim_gestao_ordenador': 6, 
        'nome_ordenador': 6, 
        'numero_expediente_nomeacao': 6, 
        'tipo_cargo': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade_gestora = models.CharField(
        'Código da Unidade Gestora', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_ingresso = models.CharField(
        'Código de Ingresso', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_vinculo = models.CharField(
        'Código do Vinculo', 
        max_length=500, )
    cpf_servidor = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_inclusao_unidade_orcamentaria = models.CharField(
        'Data de Inclusão da Unidade Orçamentária', 
        max_length=500, )
    data_inicio_gestao_ordenador = models.CharField(
        'Data de Início da Gestão do Ordenador', 
        max_length=500, )
    data_referencia_ordenador = models.CharField(
        'Data de Referência do Ordenador', 
        max_length=500, )
    data_fim_gestao_ordenador = models.CharField(
        'Data de Término da Gestão do Ordenador', 
        max_length=500, )
    nome_ordenador = models.CharField(
        'Nome do Ordenador', 
        max_length=500, )
    numero_expediente_nomeacao = models.CharField(
        'Número do Expediente da Nomeação', 
        max_length=500, )
    tipo_cargo = models.CharField(
        'Tipo de Cargo', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade_gestora, self.codigo_unidade, self.codigo_ingresso, self.codigo_municipio, self.codigo_orgao, self.codigo_vinculo, self.cpf_servidor, self.data_inclusao_unidade_orcamentaria, self.data_inicio_gestao_ordenador, self.data_referencia_ordenador, self.data_fim_gestao_ordenador, self.nome_ordenador, self.numero_expediente_nomeacao, self.tipo_cargo)

    class Meta:
        verbose_name = 'Ordenador'
        verbose_name_plural = 'Ordenadores'



class TcmOrgaos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'cgc_orgao': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_tipo_unidade': 6, 
        'nome_orgao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    cgc_orgao = models.CharField(
        'CNPJ', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_tipo_unidade = models.CharField(
        'Código do Tipo de Unidade', 
        max_length=500, )
    nome_orgao = models.CharField(
        'Nome do Órgão', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.cgc_orgao, self.codigo_municipio, self.codigo_orgao, self.codigo_tipo_unidade, self.nome_orgao)

    class Meta:
        verbose_name = 'Órgão'
        verbose_name_plural = 'Órgãos'



class TcmParametros(BaseModel):
    cols = {
        'codigo': 6, 
        'descricao': 6, 
        'entrada': 6, 
        'metodo': 6, 
        'nome': 6, 
        'requerido': 6, 
        'tipo': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=500, )
    descricao = models.TextField(
        'Descrição', )
    entrada = models.CharField(
        'Entrada', 
        max_length=500, )
    metodo = models.CharField(
        'Método', 
        max_length=500, )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    requerido = models.CharField(
        'Requerido', 
        max_length=500, )
    tipo = models.CharField(
        'Tipo', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(self.codigo, self.descricao, self.entrada, self.metodo, self.nome, self.requerido, self.tipo)

    class Meta:
        verbose_name = 'Parâmetro'
        verbose_name_plural = 'Parâmetros'



class TcmProcessosGestores(BaseModel):
    cols = {
        'exercicio': 6, 
        'codigo_gestor': 6, 
        'codigo_municipio': 6, 
        'gestor': 6, 
        'municipio': 6, 
        'natureza_processo': 6, 
        'nota_improbidade': 6, 
        'processo': 6, }
    
    exercicio = models.CharField(
        'Ano de Exercício', 
        max_length=500, )
    codigo_gestor = models.CharField(
        'Código do Gestor', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    gestor = models.CharField(
        'Gestor', 
        max_length=500, )
    municipio = models.CharField(
        'Município', 
        max_length=500, )
    natureza_processo = models.CharField(
        'Natureza do Processo', 
        max_length=500, )
    nota_improbidade = models.CharField(
        'Nota de Improbidade', 
        max_length=500, )
    processo = models.CharField(
        'Processo', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio, self.codigo_gestor, self.codigo_municipio, self.gestor, self.municipio, self.natureza_processo, self.nota_improbidade, self.processo)

    class Meta:
        verbose_name = 'Processos do Gestor'
        verbose_name_plural = 'Processos dos Gestores'



class TcmProgramas(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_municipio': 6, 
        'codigo_programa': 6, 
        'nome_programa': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    nome_programa = models.CharField(
        'Nome do Programa', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_municipio, self.codigo_programa, self.nome_programa)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'



class TcmPublicacoesEditaisLicitacoes(BaseModel):
    cols = {
        'codigo_publicacao_edital': 6, 
        'codigo_municipio': 6, 
        'data_publicacao_edital': 6, 
        'data_realizacao_licitacao': 6, 
        'descricao_publicacao_edital': 6, 
        'numero_licitacao': 6, 
        'numero_sequencial_publicacao_edital': 6, }
    
    codigo_publicacao_edital = models.CharField(
        'Código da Publicação do Edital', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    data_publicacao_edital = models.CharField(
        'Data de Publicação do Edital', 
        max_length=500, )
    data_realizacao_licitacao = models.CharField(
        'Data de Realizaçao da Licitação', 
        max_length=500, )
    descricao_publicacao_edital = models.TextField(
        'Descrição da Publicação do Edital', )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=500, )
    numero_sequencial_publicacao_edital = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(self.codigo_publicacao_edital, self.codigo_municipio, self.data_publicacao_edital, self.data_realizacao_licitacao, self.descricao_publicacao_edital, self.numero_licitacao, self.numero_sequencial_publicacao_edital)

    class Meta:
        verbose_name = 'Publicação de Edital de Licitação'
        verbose_name_plural = 'Publicações de Editais de Licitações'



class TcmRealocacoesOrcamentarias(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_projeto_atividade': 6, 
        'codigo_fonte': 6, 
        'codigo_funcao': 6, 
        'codigo_subfuncao': 6, 
        'codigo_unidade': 6, 
        'codigo_elemento': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_programa': 6, 
        'data_alteracao': 6, 
        'data_referencia': 6, 
        'numero_lei': 6, 
        'numero_projeto_atividade': 6, 
        'numero_sub_projeto_atividade': 6, 
        'numero_sequencia': 6, 
        'tipo_fonte': 6, 
        'tipo_realocacao': 6, 
        'valor_realocado': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=500, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=500, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_elemento = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=500, )
    data_alteracao = models.CharField(
        'Data de Alteração', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    numero_lei = models.CharField(
        'Número da Lei', 
        max_length=500, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=500, )
    numero_sub_projeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=500, )
    numero_sequencia = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    tipo_realocacao = models.CharField(
        'Tipo de Realocação', 
        max_length=500, )
    valor_realocado = models.DecimalField(
        'Valor Realocado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_projeto_atividade, self.codigo_fonte, self.codigo_funcao, self.codigo_subfuncao, self.codigo_unidade, self.codigo_elemento, self.codigo_municipio, self.codigo_orgao, self.codigo_programa, self.data_alteracao, self.data_referencia, self.numero_lei, self.numero_projeto_atividade, self.numero_sub_projeto_atividade, self.numero_sequencia, self.tipo_fonte, self.tipo_realocacao, self.valor_realocado)

    class Meta:
        verbose_name = 'Realocação Orçamentária'
        verbose_name_plural = 'Realocações Orçamentárias'



class TcmReavalBaixasBens(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_ingresso': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_vinculo': 6, 
        'cpf_servidor_municipal': 6, 
        'data_avaliacao': 6, 
        'data_referencia': 6, 
        'descricao_motivo': 6, 
        'numero_expediente': 6, 
        'numero_registro_bem': 6, 
        'status_situacao_bem': 6, 
        'valor_avaliacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_ingresso = models.CharField(
        'Código de Ingresso', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_vinculo = models.CharField(
        'Código do Vinculo', 
        max_length=500, )
    cpf_servidor_municipal = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_avaliacao = models.CharField(
        'Data de Avaliação', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    descricao_motivo = models.TextField(
        'Descrição do Motivo', )
    numero_expediente = models.CharField(
        'Número do Expediente', 
        max_length=500, )
    numero_registro_bem = models.CharField(
        'Número do Registro do Bem', 
        max_length=500, )
    status_situacao_bem = models.CharField(
        'Status da Situação do Bem', 
        max_length=500, )
    valor_avaliacao = models.DecimalField(
        'Valor da Avaliação',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_ingresso, self.codigo_municipio, self.codigo_orgao, self.codigo_vinculo, self.cpf_servidor_municipal, self.data_avaliacao, self.data_referencia, self.descricao_motivo, self.numero_expediente, self.numero_registro_bem, self.status_situacao_bem, self.valor_avaliacao)

    class Meta:
        verbose_name = 'Reavaliação de Baixa de Bens'
        verbose_name_plural = 'Reavaliações de Baixas de Bens'



class TcmRecursosEmpenhos(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'data_celebracao_convenio': 6, 
        'data_emissao_empenho': 6, 
        'numero_empenho': 6, 
        'numero_sequencial_recurso': 6, 
        'numero_sequencial_convenio': 6, 
        'tipo_recurso_empenho': 6, 
        'valor_recurso_empenho': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    data_celebracao_convenio = models.CharField(
        'Data de Celebração do Convênio', 
        max_length=500, )
    data_emissao_empenho = models.CharField(
        'Data de Emissão do Empenho', 
        max_length=500, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=500, )
    numero_sequencial_recurso = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    numero_sequencial_convenio = models.CharField(
        'Número Sequencial', 
        max_length=500, )
    tipo_recurso_empenho = models.CharField(
        'Tipo de Recurso do Empenho', 
        max_length=500, )
    valor_recurso_empenho = models.DecimalField(
        'Valor do Recurso do Empenho',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.data_celebracao_convenio, self.data_emissao_empenho, self.numero_empenho, self.numero_sequencial_recurso, self.numero_sequencial_convenio, self.tipo_recurso_empenho, self.valor_recurso_empenho)

    class Meta:
        verbose_name = 'Recurso de Empenho'
        verbose_name_plural = 'Recursos de Empenhos'



class TcmTaloesExtras(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'cd_conta_ctx': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'dt_credito_tx': 6, 
        'dt_ref_tx': 6, 
        'dt_talao_receita_tx': 6, 
        'de_hist_receita_tx': 6, 
        'nu_agencia_bancaria_tx': 6, 
        'nu_conta_corrente_tx': 6, 
        'nu_banco_tx': 6, 
        'nu_doc_contrib_tx': 6, 
        'nu_doc_credito_tx': 6, 
        'nu_talao_receita_tx': 6, 
        'nm_razao_social_contrib_tx': 6, 
        'tp_doc_credito_tx': 6, 
        'tp_doc_contrib_tx': 6, 
        'vl_receita_tx': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    cd_conta_ctx = models.CharField(
        'Código Conta CTX', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    dt_credito_tx = models.CharField(
        'Data de Crédito', 
        max_length=500, )
    dt_ref_tx = models.CharField(
        'Data de Referência', 
        max_length=500, )
    dt_talao_receita_tx = models.CharField(
        'Data do Talão Extra', 
        max_length=500, )
    de_hist_receita_tx = models.CharField(
        'de_hist_receita_tx', 
        max_length=500, )
    nu_agencia_bancaria_tx = models.CharField(
        'Número da Agência', 
        max_length=500, )
    nu_conta_corrente_tx = models.CharField(
        'Número da Conta-Corrente', 
        max_length=500, )
    nu_banco_tx = models.CharField(
        'Número do Banco', 
        max_length=500, )
    nu_doc_contrib_tx = models.CharField(
        'Número do Documento de Contribuição', 
        max_length=500, )
    nu_doc_credito_tx = models.CharField(
        'Número do Documento de Crédito', 
        max_length=500, )
    nu_talao_receita_tx = models.CharField(
        'Número do Talão da Receita', 
        max_length=500, )
    nm_razao_social_contrib_tx = models.CharField(
        'Razão Social do Contribuinte', 
        max_length=500, )
    tp_doc_credito_tx = models.CharField(
        'Tipo de Documento de Crédito', 
        max_length=500, )
    tp_doc_contrib_tx = models.CharField(
        'Tipo de Documento do Contribuinte', 
        max_length=500, )
    vl_receita_tx = models.DecimalField(
        'Valor da Receita',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.cd_conta_ctx, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.dt_credito_tx, self.dt_ref_tx, self.dt_talao_receita_tx, self.de_hist_receita_tx, self.nu_agencia_bancaria_tx, self.nu_conta_corrente_tx, self.nu_banco_tx, self.nu_doc_contrib_tx, self.nu_doc_credito_tx, self.nu_talao_receita_tx, self.nm_razao_social_contrib_tx, self.tp_doc_credito_tx, self.tp_doc_contrib_tx, self.vl_receita_tx)

    class Meta:
        verbose_name = 'Talão Extra'
        verbose_name_plural = 'Talões Extras'



class TcmTaloesReceitas(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_fonte': 6, 
        'codigo_rubrica': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'dt_credito_tr': 6, 
        'data_referencia': 6, 
        'data_talao_receita': 6, 
        'historico_receita': 6, 
        'numero_agencia_bancaria': 6, 
        'numero_conta_corrente': 6, 
        'numero_banco': 6, 
        'numero_doc_credito': 6, 
        'numero_doc_contribuinte': 6, 
        'numero_talao_receita': 6, 
        'nome_razao_social_contribuinte': 6, 
        'tipo_doc_credito': 6, 
        'tipo_doc_contribuinte': 6, 
        'tipo_fonte': 6, 
        'valor_receita': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=500, )
    codigo_rubrica = models.CharField(
        'Código da Rubrica', 
        max_length=500, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    dt_credito_tr = models.CharField(
        'Data de Crédito', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    data_talao_receita = models.CharField(
        'Data do Talão da Receita', 
        max_length=500, )
    historico_receita = models.CharField(
        'Histórico da Receita', 
        max_length=500, )
    numero_agencia_bancaria = models.CharField(
        'Número da Agência', 
        max_length=500, )
    numero_conta_corrente = models.CharField(
        'Número da Conta-Corrente', 
        max_length=500, )
    numero_banco = models.CharField(
        'Número do Banco', 
        max_length=500, )
    numero_doc_credito = models.CharField(
        'Número do Documento de Crédito', 
        max_length=500, )
    numero_doc_contribuinte = models.CharField(
        'Número do Documento do Contribuinte', 
        max_length=500, )
    numero_talao_receita = models.CharField(
        'Número do Talão da Receita', 
        max_length=500, )
    nome_razao_social_contribuinte = models.CharField(
        'Razão Social do Contribuinte', 
        max_length=500, )
    tipo_doc_credito = models.CharField(
        'Tipo de Documento de Crédito', 
        max_length=500, )
    tipo_doc_contribuinte = models.CharField(
        'Tipo de Documento do Contribuinte', 
        max_length=500, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=500, )
    valor_receita = models.DecimalField(
        'Valor da Receita',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_fonte, self.codigo_rubrica, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.dt_credito_tr, self.data_referencia, self.data_talao_receita, self.historico_receita, self.numero_agencia_bancaria, self.numero_conta_corrente, self.numero_banco, self.numero_doc_credito, self.numero_doc_contribuinte, self.numero_talao_receita, self.nome_razao_social_contribuinte, self.tipo_doc_credito, self.tipo_doc_contribuinte, self.tipo_fonte, self.valor_receita)

    class Meta:
        verbose_name = 'Talão de Receita'
        verbose_name_plural = 'Talões de Receitas'



class TcmTipos(BaseModel):
    cols = {
        'codigo': 6, 
        'descricao': 6, 
        'nome': 6, }
    
    codigo = models.CharField(
        'Código', 
        max_length=500, )
    descricao = models.TextField(
        'Descrição', )
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.codigo, self.descricao, self.nome)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'



class TcmTiposUnidadesAdministrativas(BaseModel):
    cols = {
        'codigo_tipo_unidade_administrativa': 6, 
        'nome_tipo_unidade_administrativa': 6, }
    
    codigo_tipo_unidade_administrativa = models.CharField(
        'Código do Tipo de Unidade', 
        max_length=500, )
    nome_tipo_unidade_administrativa = models.CharField(
        'Tipo de Unidade Administrativa', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {}'.format(self.codigo_tipo_unidade_administrativa, self.nome_tipo_unidade_administrativa)

    class Meta:
        verbose_name = 'Tipo de Unidade Administrativa'
        verbose_name_plural = 'Tipos de Unidades Administrativas'



class TcmUnidadeOrcamentariaBens(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_ingresso': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_vinculo': 6, 
        'cpf_servidor_municipal': 6, 
        'data_disponibilizacao': 6, 
        'data_referencia': 6, 
        'numero_expediente': 6, 
        'numero_registro_bem': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_ingresso = models.CharField(
        'Código de Ingresso', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_vinculo = models.CharField(
        'Código do Vinculo', 
        max_length=500, )
    cpf_servidor_municipal = models.CharField(
        'CPF do Servidor', 
        max_length=500, )
    data_disponibilizacao = models.CharField(
        'Data de Disponibilização', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    numero_expediente = models.CharField(
        'Número do Expediente', 
        max_length=500, )
    numero_registro_bem = models.CharField(
        'Número do Registro do Bem', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_ingresso, self.codigo_municipio, self.codigo_orgao, self.codigo_vinculo, self.cpf_servidor_municipal, self.data_disponibilizacao, self.data_referencia, self.numero_expediente, self.numero_registro_bem)

    class Meta:
        verbose_name = 'Bem da Unidade Orçamentária'
        verbose_name_plural = 'Bens da Unidade Orçamentária'



class TcmUnidadesFederacao(BaseModel):
    cols = {
        'codigo_unidade_federacao': 6, 
        'nome_unidade_federacao': 6, 
        'sigla_unidade_federacao': 6, }
    
    codigo_unidade_federacao = models.CharField(
        'Código da Unidade Federação', 
        max_length=500, )
    nome_unidade_federacao = models.CharField(
        'Nome da Unidade da Federação', 
        max_length=500, )
    sigla_unidade_federacao = models.CharField(
        'Sigla', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.codigo_unidade_federacao, self.nome_unidade_federacao, self.sigla_unidade_federacao)

    class Meta:
        verbose_name = 'Unidade da Federação'
        verbose_name_plural = 'Unidades da Federação'



class TcmUnidadesGestoras(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_municipio': 6, 
        'codigo_unidade_gestora': 6, 
        'data_referencia': 6, 
        'nome_unidade_gestora': 6, 
        'data_criacao': 6, 
        'data_extincao': 6, 
        'numero_lei_criacao': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_unidade_gestora = models.CharField(
        'Código da Unidade Gestora', 
        max_length=500, )
    data_referencia = models.CharField(
        'Data de Referência', 
        max_length=500, )
    nome_unidade_gestora = models.CharField(
        'Nome da Unidade Gestora', 
        max_length=500, )
    data_criacao = models.CharField(
        'Data de Criação', 
        max_length=500, )
    data_extincao = models.CharField(
        'Data de Extinção', 
        max_length=500, )
    numero_lei_criacao = models.CharField(
        'Número da Lei de Criação', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_municipio, self.codigo_unidade_gestora, self.data_referencia, self.nome_unidade_gestora, self.data_criacao, self.data_extincao, self.numero_lei_criacao)

    class Meta:
        verbose_name = 'Unidade Gestora'
        verbose_name_plural = 'Unidades Gestoras'



class TcmUnidadesOrcamentarias(BaseModel):
    cols = {
        'exercicio_orcamento': 6, 
        'codigo_unidade': 6, 
        'codigo_municipio': 6, 
        'codigo_orgao': 6, 
        'codigo_tipo_unidade': 6, 
        'nome_unidade': 6, 
        'tipo_administracao_unidade': 6, }
    
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=500, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=500, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=500, )
    codigo_tipo_unidade = models.CharField(
        'Código do Tipo de Unidade', 
        max_length=500, )
    nome_unidade = models.CharField(
        'Nome da Unidade', 
        max_length=500, )
    tipo_administracao_unidade = models.CharField(
        'Tipo de Administração', 
        max_length=500, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.codigo_tipo_unidade, self.nome_unidade, self.tipo_administracao_unidade)

    class Meta:
        verbose_name = 'Unidade Orçamentária'
        verbose_name_plural = 'Unidades Orçamentárias'



class AspecEmpenhos(BaseModel):
    cols = {
        'numero': 6, 
        'data': 6, 
        'tipo': 6, 
        'credor_nome': 6, 
        'credor_cnpj': 6, 
        'licitacao_modalidade': 6, 
        'licitacao_numero': 6, 
        'unidade_orcamentaria_codigo': 6, 
        'unidade_orcamentaria_titulo': 6, 
        'funcao_codigo': 6, 
        'funcao_titulo': 6, 
        'subfuncao_codigo': 6, 
        'subfuncao_titulo': 6, 
        'programa_codigo': 6, 
        'programa_titulo': 6, 
        'acao_codigo': 6, 
        'acao_titulo': 6, 
        'elemento_despesa_codigo': 6, 
        'elemento_despesa_titulo': 6, 
        'fonte': 6, 
        'historico': 6, }
    
    numero = models.CharField(
        'Número', 
        max_length=20, )
    data = models.DateField(
        'Data', )
    tipo = models.CharField(
        'Tipo', 
        max_length=50, )
    credor_nome = models.CharField(
        'Nome do Credor', 
        max_length=200, )
    credor_cnpj = models.CharField(
        'CNPJ do Credor', 
        max_length=20, )
    licitacao_modalidade = models.CharField(
        'Modalidade de Licitação', 
        max_length=20, )
    licitacao_numero = models.CharField(
        'Número da Licitação', 
        max_length=20, )
    unidade_orcamentaria_codigo = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=20, )
    unidade_orcamentaria_titulo = models.CharField(
        'Título da Unidade Orçamentária', 
        max_length=200, )
    funcao_codigo = models.CharField(
        'Código da Função', 
        max_length=20, )
    funcao_titulo = models.CharField(
        'Título da Função', 
        max_length=200, )
    subfuncao_codigo = models.CharField(
        'Código da Subfunção', 
        max_length=20, )
    subfuncao_titulo = models.CharField(
        'Título da Subfunção', 
        max_length=200, )
    programa_codigo = models.CharField(
        'Código do Programa', 
        max_length=20, )
    programa_titulo = models.CharField(
        'Título do Programa', 
        max_length=200, )
    acao_codigo = models.CharField(
        'Código da Ação', 
        max_length=20, )
    acao_titulo = models.CharField(
        'Título da Ação', 
        max_length=200, )
    elemento_despesa_codigo = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=20, )
    elemento_despesa_titulo = models.CharField(
        'Título do Elemento de Despesa', 
        max_length=200, )
    fonte = models.CharField(
        'Fonte', 
        max_length=200, )
    historico = models.TextField(
        'Histórico', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.numero, self.data, self.tipo, self.credor_nome, self.credor_cnpj, self.licitacao_modalidade, self.licitacao_numero, self.unidade_orcamentaria_codigo, self.unidade_orcamentaria_titulo, self.funcao_codigo, self.funcao_titulo, self.subfuncao_codigo, self.subfuncao_titulo, self.programa_codigo, self.programa_titulo, self.acao_codigo, self.acao_titulo, self.elemento_despesa_codigo, self.elemento_despesa_titulo, self.fonte, self.historico)

    class Meta:
        verbose_name = 'Empenho'
        verbose_name_plural = 'Empenhos'



class AspecEmpenhosMovimentos(BaseModel):
    cols = {
        'aspec_empenho': 6, 
        'documento': 6, 
        'data': 6, 
        'tipo': 6, 
        'registro': 6, 
        'valor': 6, }
    
    aspec_empenho = models.ForeignKey(
        'dados_externos.AspecEmpenhos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_aspec_empenho', )
    documento = models.CharField(
        'Documento', 
        max_length=20, )
    data = models.DateField(
        'Data', )
    tipo = models.CharField(
        'Tipo', 
        max_length=20, )
    registro = models.CharField(
        'Registro', 
        max_length=20, )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.aspec_empenho, self.documento, self.data, self.tipo, self.registro, self.valor)

    class Meta:
        verbose_name = 'Movimento dos Empenho'
        verbose_name_plural = 'Movimentos dos Empenhos'



class AspecLiquidacoes(BaseModel):
    cols = {
        'numero': 6, 
        'data': 6, 
        'valor': 6, 
        'nota_fiscal_numero': 6, 
        'nota_fiscal_serie': 6, 
        'nota_fiscal_tipo': 6, 
        'nota_fiscal_data': 6, }
    
    numero = models.CharField(
        'Número', 
        max_length=20, )
    data = models.DateField(
        'Data', )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    nota_fiscal_numero = models.CharField(
        'Número da Nota-Fiscal', 
        max_length=20, )
    nota_fiscal_serie = models.CharField(
        'Série da Nota-Fiscal', 
        max_length=2, )
    nota_fiscal_tipo = models.CharField(
        'Tipo da Nota-Fiscal', 
        max_length=50, )
    nota_fiscal_data = models.DateField(
        'Data da Nota-Fiscal', )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(self.numero, self.data, self.valor, self.nota_fiscal_numero, self.nota_fiscal_serie, self.nota_fiscal_tipo, self.nota_fiscal_data)

    class Meta:
        verbose_name = 'Liquidação'
        verbose_name_plural = 'Liquidações'



class AspecLiquidacoesItens(BaseModel):
    cols = {
        'aspec_liquidacao': 6, 
        'descricao_item': 6, 
        'quantidade': 6, 
        'unidade': 6, 
        'valor_unitario': 6, 
        'valor_total': 6, }
    
    aspec_liquidacao = models.ForeignKey(
        'dados_externos.AspecLiquidacoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_aspec_liquidacao', )
    descricao_item = models.CharField(
        'Descrição do Item', 
        max_length=200, )
    quantidade = models.DecimalField(
        'Quantidade',  
        max_digits=15, 
        decimal_places=2, )
    unidade = models.CharField(
        'Unidade', 
        max_length=20, )
    valor_unitario = models.DecimalField(
        'Valor Unitário',  
        max_digits=15, 
        decimal_places=2, )
    valor_total = models.DecimalField(
        'Valor Total',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.aspec_liquidacao, self.descricao_item, self.quantidade, self.unidade, self.valor_unitario, self.valor_total)

    class Meta:
        verbose_name = 'Item das Liquidação'
        verbose_name_plural = 'Itens das Liquidações'



class AspecPagamentos(BaseModel):
    cols = {
        'numero': 6, 
        'data_liquidacao': 6, 
        'valor_total': 6, }
    
    numero = models.CharField(
        'Número', 
        max_length=20, )
    data_liquidacao = models.DateField(
        'Data da Liquidação', )
    valor_total = models.DecimalField(
        'Valor total do Pagamento',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.numero, self.data_liquidacao, self.valor_total)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'



class AspecPagamentosDetalhes(BaseModel):
    cols = {
        'aspec_pagamentos': 6, 
        'tipo': 6, 
        'forma': 6, 
        'valor': 6, 
        'documento_numero': 6, 
        'banco_nome': 6, 
        'agencia_nome': 6, 
        'agencia_numero': 6, 
        'conta_corrente_numero': 6, }
    
    aspec_pagamentos = models.ForeignKey(
        'dados_externos.AspecPagamentos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_aspec_pagamentos', )
    tipo = models.CharField(
        'Tipo', 
        max_length=20, )
    forma = models.CharField(
        'Forma', 
        max_length=20, )
    valor = models.DecimalField(
        'Valor',  
        max_digits=15, 
        decimal_places=2, )
    documento_numero = models.CharField(
        'Número do Documento', 
        max_length=20, )
    banco_nome = models.CharField(
        'Nome do Banco', 
        max_length=50, )
    agencia_nome = models.CharField(
        'Nome da Agência', 
        max_length=100, )
    agencia_numero = models.CharField(
        'Número da Agência', 
        max_length=20, )
    conta_corrente_numero = models.CharField(
        'Número da Conta-Corrente', 
        max_length=20, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.aspec_pagamentos, self.tipo, self.forma, self.valor, self.documento_numero, self.banco_nome, self.agencia_nome, self.agencia_numero, self.conta_corrente_numero)

    class Meta:
        verbose_name = 'Detalhe dos Pagamento'
        verbose_name_plural = 'Detalhes dos Pagamentos'