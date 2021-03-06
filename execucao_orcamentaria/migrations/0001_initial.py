# Generated by Django 3.2 on 2022-03-26 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planejamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empenhos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('exercicio_orcamento', models.CharField(max_length=6, verbose_name='Ano de Exercício do Orçamento')),
                ('cep_negociante', models.CharField(max_length=8, verbose_name='CEP')),
                ('codigo_projeto_atividade', models.CharField(max_length=20, verbose_name='Código da Ação')),
                ('codigo_fonte', models.CharField(max_length=20, verbose_name='Código da Fonte')),
                ('codigo_funcao', models.CharField(max_length=20, verbose_name='Código da Função')),
                ('codigo_subfuncao', models.CharField(max_length=20, verbose_name='Código da SubFunção')),
                ('codigo_unidade', models.CharField(max_length=20, verbose_name='Código da Unidade Orçamentária')),
                ('codigo_elemento_despesa', models.CharField(max_length=20, verbose_name='Código do Elemento de Despesa')),
                ('codigo_municipio', models.CharField(max_length=20, verbose_name='Código do Município')),
                ('codigo_orgao', models.CharField(max_length=20, verbose_name='Código do Órgão')),
                ('codigo_programa', models.CharField(max_length=20, verbose_name='Código do Programa')),
                ('codigo_tipo_negociante', models.CharField(max_length=20, verbose_name='Código do Tipo de Negociante')),
                ('cpf_gestor_contrato', models.CharField(max_length=11, verbose_name='CPF do Gestor do Contrato')),
                ('cd_cpf_gestor', models.CharField(max_length=20, verbose_name='CPF Gestor')),
                ('data_emissao_empenho', models.DateField(verbose_name='Data de Emissão do Empenho')),
                ('data_emissao_empenho_substituto', models.DateField(verbose_name='Data de Emissão do Empenho Substituto')),
                ('data_realizacao_licitacao', models.DateField(verbose_name='Data de Realização da Licitação')),
                ('data_referencia_empenho', models.DateField(verbose_name='Data de Referência do Empenho')),
                ('data_contrato', models.DateField(verbose_name='Data do Contrato')),
                ('descricao_empenho', models.TextField(verbose_name='Descrição do Empenho')),
                ('endereco_negociante', models.CharField(max_length=20, verbose_name='Endereço do Negociante')),
                ('estado_empenho', models.CharField(max_length=20, verbose_name='Estado do Empenho')),
                ('modalidade_empenho', models.CharField(max_length=20, verbose_name='Modalidade do Empenho')),
                ('nome_municipio_negociante', models.CharField(max_length=200, verbose_name='Nome do Município do Negociante')),
                ('nome_negociante', models.CharField(max_length=200, verbose_name='Nome do Negociante')),
                ('numero_licitacao', models.CharField(max_length=20, verbose_name='Número da Licitação')),
                ('numero_nota_anulacao', models.CharField(max_length=20, verbose_name='Número da Nota de Anulação')),
                ('numero_contrato', models.CharField(max_length=20, verbose_name='Número do Contrato')),
                ('numero_documento_negociante', models.CharField(max_length=20, verbose_name='Número do Documento do Negociante')),
                ('numero_empenho', models.CharField(max_length=20, verbose_name='Número do Empenho')),
                ('numero_empenho_substituto', models.CharField(max_length=20, verbose_name='Número do Empenho Substituto')),
                ('numero_projeto_atividade', models.CharField(max_length=20, verbose_name='Número do Projeto-Atividade')),
                ('numero_subprojeto_atividade', models.CharField(max_length=20, verbose_name='Número do Sub-Projeto-Atividade')),
                ('fone_negociante', models.CharField(max_length=20, verbose_name='Telefone do Negociante')),
                ('tipo_fonte', models.CharField(max_length=20, verbose_name='Tipo de Fonte')),
                ('tipo_processo_licitatorio', models.IntegerField(choices=[(1, 'Nao Definido')], verbose_name='Tipo do Processo Licitatório')),
                ('codigo_uf', models.CharField(max_length=20, verbose_name='UF')),
                ('valor_anterior_saldo_dotacao', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Anterior do Saldo da Dotação')),
                ('valor_atual_saldo_dotacao', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Atual do Saldo da Dotação')),
                ('valor_empenhado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Empenhado')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='empenhos_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='empenhos_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empenho',
                'verbose_name_plural': 'Empenhos',
            },
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('exercicio_orcamento', models.CharField(max_length=6, verbose_name='Ano de Exercício do Orçamento')),
                ('codigo_unidade', models.CharField(max_length=20, verbose_name='Código da Unidade Orçamentária')),
                ('codigo_municipio', models.CharField(max_length=20, verbose_name='Código do Município')),
                ('codigo_orgao', models.CharField(max_length=20, verbose_name='Código do Órgão')),
                ('cpf_pagador', models.CharField(max_length=11, verbose_name='CPF do Pagador')),
                ('data_nota_pagamento', models.DateField(verbose_name='Data da Nota de Pagamento')),
                ('data_emissao_empenho', models.DateField(verbose_name='Data de Emissão do Empenho')),
                ('data_referencia', models.DateField(verbose_name='Data de Referência')),
                ('estado_de_estornado', models.CharField(max_length=20, verbose_name='Estado de Estornado')),
                ('nome_pagador', models.CharField(max_length=200, verbose_name='Nome do Pagador')),
                ('numero_nota_pagamento', models.CharField(max_length=20, verbose_name='Número da Nota de Pagamento')),
                ('nu_documento_caixa', models.CharField(max_length=20, verbose_name='Número do Documento de Caixa')),
                ('numero_empenho', models.CharField(max_length=20, verbose_name='Número do Empenho')),
                ('numero_sub_empenho', models.CharField(max_length=20, verbose_name='Número do Sub-Empenho')),
                ('valor_nota_pagamento', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor da Nota de Pagamento')),
                ('valor_empenhado_a_pagar', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Empenhado a Pagar')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagamentos_created_by', to=settings.AUTH_USER_MODEL)),
                ('liquidacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pagamentos_liquidacao', to='execucao_orcamentaria.empenhos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagamentos_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='OrcamentosExecucaoReceitasMensais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('mes', models.IntegerField(verbose_name='Mês de Referência')),
                ('valor_arrecadado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Arrecadado')),
                ('valor_arrecadacao_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Arrecadado Anulado')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaoreceitasmensais_created_by', to=settings.AUTH_USER_MODEL)),
                ('orcamento_receitas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orcamentosexecucaoreceitasmensais_orcamento_receitas', to='planejamento.orcamentosreceitas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaoreceitasmensais_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Execução Orçamentária das Receitas Mensais',
                'verbose_name_plural': 'Execução Orçamentária das Receitas Mensais',
            },
        ),
        migrations.CreateModel(
            name='OrcamentosExecucaoReceitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('valor_arrecadado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Arrecadado')),
                ('valor_arrecadacao_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Arrecadado Anulado')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaoreceitas_created_by', to=settings.AUTH_USER_MODEL)),
                ('orcamento_receitas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orcamentosexecucaoreceitas_orcamento_receitas', to='planejamento.orcamentosreceitas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaoreceitas_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Execução Orçamentária das Receitas',
                'verbose_name_plural': 'Execução Orçamentária das Receitas',
            },
        ),
        migrations.CreateModel(
            name='OrcamentosExecucaoDespesasMensais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('mes', models.IntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Marco'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')], verbose_name='Mês de Referência')),
                ('valor_dotacao_suplementado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Suplementado na Dotação')),
                ('valor_dotacao_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Anulado na Dotação')),
                ('valor_empenhado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Empenhado')),
                ('valor_empenhado_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor das Anulações dos Empenhos')),
                ('valor_liquidado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Liquidado')),
                ('valor_liquidado_extornado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Estornos das Liquidações')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Pago')),
                ('valor_pago_extornado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Estornos dos Pagamentos')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaodespesasmensais_created_by', to=settings.AUTH_USER_MODEL)),
                ('orcamento_despesas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orcamentosexecucaodespesasmensais_orcamento_despesas', to='planejamento.orcamentosdespesas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaodespesasmensais_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Execução Orçamentária das Despesas Mensais',
                'verbose_name_plural': 'Execução Orçamentária das Despesas Mensais',
            },
        ),
        migrations.CreateModel(
            name='OrcamentosExecucaoDespesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('valor_dotacao_suplementado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Suplementado na Dotação')),
                ('valor_dotacao_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Anulado na Dotação')),
                ('valor_empenhado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Empenhado')),
                ('valor_empenhado_anulado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor das Anulações dos Empenhos')),
                ('valor_liquidado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Liquidado')),
                ('valor_liquidado_extornado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Estornos das Liquidações')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Pago')),
                ('valor_pago_extornado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Estornos dos Pagamentos')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaodespesas_created_by', to=settings.AUTH_USER_MODEL)),
                ('orcamento_despesas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orcamentosexecucaodespesas_orcamento_despesas', to='planejamento.orcamentosdespesas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orcamentosexecucaodespesas_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Execução Orçamentária das Despesas',
                'verbose_name_plural': 'Execução Orçamentária das Despesas',
            },
        ),
        migrations.CreateModel(
            name='Liquidacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('exercicio_orcamento', models.CharField(max_length=6, verbose_name='Ano de Exercício do Orçamento')),
                ('codigo_unidade', models.CharField(max_length=20, verbose_name='Código da Unidade Orçamentária')),
                ('codigo_municipio', models.CharField(max_length=20, verbose_name='Código do Município')),
                ('codigo_orgao', models.CharField(max_length=20, verbose_name='Código do Órgão')),
                ('cpf_responsavel_liquidacao', models.CharField(max_length=11, verbose_name='CPF do Responsável pela Liquidação')),
                ('data_emissao_empenho', models.DateField(verbose_name='Data de Emissão do Empenho')),
                ('data_liquidacao', models.DateField(verbose_name='Data de Liquidação')),
                ('data_referencia_liquidacao', models.DateField(verbose_name='Data de Referência da Liquidação')),
                ('estado_folha', models.CharField(max_length=20, verbose_name='Estado da Folha')),
                ('estado_de_estorno', models.CharField(max_length=20, verbose_name='Estado de Estorno')),
                ('nome_responsavel_liquidacao', models.CharField(max_length=200, verbose_name='Nome do Responsável pela Liquidação')),
                ('numero_empenho', models.CharField(max_length=20, verbose_name='Número do Empenho')),
                ('numero_sub_empenho_liquidacao', models.CharField(max_length=20, verbose_name='Número do Sub-Empenho')),
                ('valor_liquidado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Liquidado')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='liquidacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('empenho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='liquidacoes_empenho', to='execucao_orcamentaria.empenhos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='liquidacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Liquidação',
                'verbose_name_plural': 'Liquidações',
            },
        ),
        migrations.CreateModel(
            name='Credores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=500, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('cpf_cnpj', models.CharField(max_length=50, verbose_name='CPF/CNPJ')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=500, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=50, verbose_name='Número')),
                ('municipio', models.CharField(max_length=100, verbose_name='Município')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('status', models.IntegerField(choices=[(1, 'Nao Definido')], verbose_name='Status')),
                ('cod_contribuinte', models.CharField(max_length=50, verbose_name='Código do Contribuinte')),
                ('cod_municipio', models.CharField(max_length=50, verbose_name='Código do Município')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='credores_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='credores_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Credor',
                'verbose_name_plural': 'Credores',
            },
        ),
    ]
