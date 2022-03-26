# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from config.mixins import BaseModel
from .choices import *



class Credores(BaseModel):
    cols = {
        'nome': 6, 
        'codigo': 6, 
        'cpf_cnpj': 6, 
        'telefone': 6, 
        'email': 6, 
        'cep': 6, 
        'logradouro': 6, 
        'numero': 6, 
        'municipio': 6, 
        'bairro': 6, 
        'uf': 6, 
        'status': 6, 
        'cod_contribuinte': 6, 
        'cod_municipio': 6, }
    
    nome = models.CharField(
        'Nome', 
        max_length=500, )
    codigo = models.CharField(
        'Código', 
        max_length=50, )
    cpf_cnpj = models.CharField(
        'CPF/CNPJ', 
        max_length=50, )
    telefone = models.CharField(
        'Telefone', 
        max_length=50, )
    email = models.EmailField(
        'E-mail', 
        max_length=255, )
    cep = models.CharField(
        'CEP', 
        max_length=10, )
    logradouro = models.CharField(
        'Logradouro', 
        max_length=500, )
    numero = models.CharField(
        'Número', 
        max_length=50, )
    municipio = models.CharField(
        'Município', 
        max_length=100, )
    bairro = models.CharField(
        'Bairro', 
        max_length=50, )
    uf = models.CharField(
        'UF', 
        max_length=2, )
    status = models.IntegerField(
        'Status', 
        choices=CHOICES_STATUS, )
    cod_contribuinte = models.CharField(
        'Código do Contribuinte', 
        max_length=50, )
    cod_municipio = models.CharField(
        'Código do Município', 
        max_length=50, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.nome, self.codigo, self.cpf_cnpj, self.telefone, self.email, self.cep, self.logradouro, self.numero, self.municipio, self.bairro, self.uf, self.status, self.cod_contribuinte, self.cod_municipio)

    class Meta:
        verbose_name = 'Credor'
        verbose_name_plural = 'Credores'



class Empenhos(BaseModel):
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
        max_length=8, )
    codigo_projeto_atividade = models.CharField(
        'Código da Ação', 
        max_length=20, )
    codigo_fonte = models.CharField(
        'Código da Fonte', 
        max_length=20, )
    codigo_funcao = models.CharField(
        'Código da Função', 
        max_length=20, )
    codigo_subfuncao = models.CharField(
        'Código da SubFunção', 
        max_length=20, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=20, )
    codigo_elemento_despesa = models.CharField(
        'Código do Elemento de Despesa', 
        max_length=20, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=20, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=20, )
    codigo_programa = models.CharField(
        'Código do Programa', 
        max_length=20, )
    codigo_tipo_negociante = models.CharField(
        'Código do Tipo de Negociante', 
        max_length=20, )
    cpf_gestor_contrato = models.CharField(
        'CPF do Gestor do Contrato', 
        max_length=11, )
    cd_cpf_gestor = models.CharField(
        'CPF Gestor', 
        max_length=20, )
    data_emissao_empenho = models.DateField(
        'Data de Emissão do Empenho', )
    data_emissao_empenho_substituto = models.DateField(
        'Data de Emissão do Empenho Substituto', )
    data_realizacao_licitacao = models.DateField(
        'Data de Realização da Licitação', )
    data_referencia_empenho = models.DateField(
        'Data de Referência do Empenho', )
    data_contrato = models.DateField(
        'Data do Contrato', )
    descricao_empenho = models.TextField(
        'Descrição do Empenho', )
    endereco_negociante = models.CharField(
        'Endereço do Negociante', 
        max_length=20, )
    estado_empenho = models.CharField(
        'Estado do Empenho', 
        max_length=20, )
    modalidade_empenho = models.CharField(
        'Modalidade do Empenho', 
        max_length=20, )
    nome_municipio_negociante = models.CharField(
        'Nome do Município do Negociante', 
        max_length=200, )
    nome_negociante = models.CharField(
        'Nome do Negociante', 
        max_length=200, )
    numero_licitacao = models.CharField(
        'Número da Licitação', 
        max_length=20, )
    numero_nota_anulacao = models.CharField(
        'Número da Nota de Anulação', 
        max_length=20, )
    numero_contrato = models.CharField(
        'Número do Contrato', 
        max_length=20, )
    numero_documento_negociante = models.CharField(
        'Número do Documento do Negociante', 
        max_length=20, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=20, )
    numero_empenho_substituto = models.CharField(
        'Número do Empenho Substituto', 
        max_length=20, )
    numero_projeto_atividade = models.CharField(
        'Número do Projeto-Atividade', 
        max_length=20, )
    numero_subprojeto_atividade = models.CharField(
        'Número do Sub-Projeto-Atividade', 
        max_length=20, )
    fone_negociante = models.CharField(
        'Telefone do Negociante', 
        max_length=20, )
    tipo_fonte = models.CharField(
        'Tipo de Fonte', 
        max_length=20, )
    tipo_processo_licitatorio = models.IntegerField(
        'Tipo do Processo Licitatório', 
        choices=CHOICES_TIPO_PROCESSO_LICITATORIO, )
    codigo_uf = models.CharField(
        'UF', 
        max_length=20, )
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
        verbose_name_plural = 'Empenhos'



class Liquidacoes(BaseModel):
    cols = {
        'empenho': 6, 
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
    
    empenho = models.ForeignKey(
        'execucao_orcamentaria.Empenhos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_empenho', )
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=20, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=20, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=20, )
    cpf_responsavel_liquidacao = models.CharField(
        'CPF do Responsável pela Liquidação', 
        max_length=11, )
    data_emissao_empenho = models.DateField(
        'Data de Emissão do Empenho', )
    data_liquidacao = models.DateField(
        'Data de Liquidação', )
    data_referencia_liquidacao = models.DateField(
        'Data de Referência da Liquidação', )
    estado_folha = models.CharField(
        'Estado da Folha', 
        max_length=20, )
    estado_de_estorno = models.CharField(
        'Estado de Estorno', 
        max_length=20, )
    nome_responsavel_liquidacao = models.CharField(
        'Nome do Responsável pela Liquidação', 
        max_length=200, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=20, )
    numero_sub_empenho_liquidacao = models.CharField(
        'Número do Sub-Empenho', 
        max_length=20, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.empenho, self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.cpf_responsavel_liquidacao, self.data_emissao_empenho, self.data_liquidacao, self.data_referencia_liquidacao, self.estado_folha, self.estado_de_estorno, self.nome_responsavel_liquidacao, self.numero_empenho, self.numero_sub_empenho_liquidacao, self.valor_liquidado)

    class Meta:
        verbose_name = 'Liquidação'
        verbose_name_plural = 'Liquidações'



class Pagamentos(BaseModel):
    cols = {
        'liquidacao': 6, 
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
    
    liquidacao = models.ForeignKey(
        'execucao_orcamentaria.Empenhos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_liquidacao', )
    exercicio_orcamento = models.CharField(
        'Ano de Exercício do Orçamento', 
        max_length=6, )
    codigo_unidade = models.CharField(
        'Código da Unidade Orçamentária', 
        max_length=20, )
    codigo_municipio = models.CharField(
        'Código do Município', 
        max_length=20, )
    codigo_orgao = models.CharField(
        'Código do Órgão', 
        max_length=20, )
    cpf_pagador = models.CharField(
        'CPF do Pagador', 
        max_length=11, )
    data_nota_pagamento = models.DateField(
        'Data da Nota de Pagamento', )
    data_emissao_empenho = models.DateField(
        'Data de Emissão do Empenho', )
    data_referencia = models.DateField(
        'Data de Referência', )
    estado_de_estornado = models.CharField(
        'Estado de Estornado', 
        max_length=20, )
    nome_pagador = models.CharField(
        'Nome do Pagador', 
        max_length=200, )
    numero_nota_pagamento = models.CharField(
        'Número da Nota de Pagamento', 
        max_length=20, )
    nu_documento_caixa = models.CharField(
        'Número do Documento de Caixa', 
        max_length=20, )
    numero_empenho = models.CharField(
        'Número do Empenho', 
        max_length=20, )
    numero_sub_empenho = models.CharField(
        'Número do Sub-Empenho', 
        max_length=20, )
    valor_nota_pagamento = models.DecimalField(
        'Valor da Nota de Pagamento',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_a_pagar = models.DecimalField(
        'Valor Empenhado a Pagar',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.liquidacao, self.exercicio_orcamento, self.codigo_unidade, self.codigo_municipio, self.codigo_orgao, self.cpf_pagador, self.data_nota_pagamento, self.data_emissao_empenho, self.data_referencia, self.estado_de_estornado, self.nome_pagador, self.numero_nota_pagamento, self.nu_documento_caixa, self.numero_empenho, self.numero_sub_empenho, self.valor_nota_pagamento, self.valor_empenhado_a_pagar)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'



class OrcamentosExecucaoDespesas(BaseModel):
    cols = {
        'orcamento_despesas': 6, 
        'valor_dotacao_suplementado': 6, 
        'valor_dotacao_anulado': 6, 
        'valor_empenhado': 6, 
        'valor_empenhado_anulado': 6, 
        'valor_liquidado': 6, 
        'valor_liquidado_extornado': 6, 
        'valor_pago': 6, 
        'valor_pago_extornado': 6, }
    
    orcamento_despesas = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_despesas', )
    valor_dotacao_suplementado = models.DecimalField(
        'Valor Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulado = models.DecimalField(
        'Valor Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado = models.DecimalField(
        'Valor Empenhado',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado = models.DecimalField(
        'Valor das Anulações dos Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_extornado = models.DecimalField(
        'Valor do Estornos das Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago = models.DecimalField(
        'Valor Pago',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_extornado = models.DecimalField(
        'Valor do Estornos dos Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.orcamento_despesas, self.valor_dotacao_suplementado, self.valor_dotacao_anulado, self.valor_empenhado, self.valor_empenhado_anulado, self.valor_liquidado, self.valor_liquidado_extornado, self.valor_pago, self.valor_pago_extornado)

    class Meta:
        verbose_name = 'Execução Orçamentária das Despesas'
        verbose_name_plural = 'Execução Orçamentária das Despesas'



class OrcamentosExecucaoDespesasMensais(BaseModel):
    cols = {
        'orcamento_despesas': 6, 
        'mes': 6, 
        'valor_dotacao_suplementado': 6, 
        'valor_dotacao_anulado': 6, 
        'valor_empenhado': 6, 
        'valor_empenhado_anulado': 6, 
        'valor_liquidado': 6, 
        'valor_liquidado_extornado': 6, 
        'valor_pago': 6, 
        'valor_pago_extornado': 6, }
    
    orcamento_despesas = models.ForeignKey(
        'planejamento.OrcamentosDespesas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_despesas', )
    mes = models.IntegerField(
        'Mês de Referência', 
        choices=CHOICES_MES, )
    valor_dotacao_suplementado = models.DecimalField(
        'Valor Suplementado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_dotacao_anulado = models.DecimalField(
        'Valor Anulado na Dotação',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado = models.DecimalField(
        'Valor Empenhado',  
        max_digits=15, 
        decimal_places=2, )
    valor_empenhado_anulado = models.DecimalField(
        'Valor das Anulações dos Empenhos',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado = models.DecimalField(
        'Valor Liquidado',  
        max_digits=15, 
        decimal_places=2, )
    valor_liquidado_extornado = models.DecimalField(
        'Valor do Estornos das Liquidações',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago = models.DecimalField(
        'Valor Pago',  
        max_digits=15, 
        decimal_places=2, )
    valor_pago_extornado = models.DecimalField(
        'Valor do Estornos dos Pagamentos',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(self.orcamento_despesas, self.mes, self.valor_dotacao_suplementado, self.valor_dotacao_anulado, self.valor_empenhado, self.valor_empenhado_anulado, self.valor_liquidado, self.valor_liquidado_extornado, self.valor_pago, self.valor_pago_extornado)

    class Meta:
        verbose_name = 'Execução Orçamentária das Despesas Mensais'
        verbose_name_plural = 'Execução Orçamentária das Despesas Mensais'



class OrcamentosExecucaoReceitas(BaseModel):
    cols = {
        'orcamento_receitas': 6, 
        'valor_arrecadado': 6, 
        'valor_arrecadacao_anulado': 6, }
    
    orcamento_receitas = models.ForeignKey(
        'planejamento.OrcamentosReceitas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_receitas', )
    valor_arrecadado = models.DecimalField(
        'Valor Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadacao_anulado = models.DecimalField(
        'Valor Arrecadado Anulado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {}'.format(self.orcamento_receitas, self.valor_arrecadado, self.valor_arrecadacao_anulado)

    class Meta:
        verbose_name = 'Execução Orçamentária das Receitas'
        verbose_name_plural = 'Execução Orçamentária das Receitas'



class OrcamentosExecucaoReceitasMensais(BaseModel):
    cols = {
        'orcamento_receitas': 6, 
        'mes': 6, 
        'valor_arrecadado': 6, 
        'valor_arrecadacao_anulado': 6, }
    
    orcamento_receitas = models.ForeignKey(
        'planejamento.OrcamentosReceitas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_orcamento_receitas', )
    mes = models.IntegerField(
        'Mês de Referência', )
    valor_arrecadado = models.DecimalField(
        'Valor Arrecadado',  
        max_digits=15, 
        decimal_places=2, )
    valor_arrecadacao_anulado = models.DecimalField(
        'Valor Arrecadado Anulado',  
        max_digits=15, 
        decimal_places=2, )
    
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.orcamento_receitas, self.mes, self.valor_arrecadado, self.valor_arrecadacao_anulado)

    class Meta:
        verbose_name = 'Execução Orçamentária das Receitas Mensais'
        verbose_name_plural = 'Execução Orçamentária das Receitas Mensais'