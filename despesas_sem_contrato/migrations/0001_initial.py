# Generated by Django 3.2 on 2022-03-26 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros_basicos', '0001_initial'),
        ('dispositivos_de_contratacao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planejamento', '0001_initial'),
        ('controle', '0001_initial'),
        ('execucao_orcamentaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DespesasSemContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('cod_orgao', models.CharField(max_length=50, verbose_name='Código do Órgão')),
                ('objeto', models.TextField(verbose_name='Objeto')),
                ('justificativa', models.TextField(verbose_name='Justificativa')),
                ('fundamentacao', models.TextField(verbose_name='Fundamentação')),
                ('num_documento', models.CharField(max_length=50, verbose_name='Número do Documento')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('classificacao', models.CharField(max_length=50, verbose_name='Classificação')),
                ('num_processo', models.CharField(max_length=50, verbose_name='Número do Processo')),
                ('status', models.IntegerField(choices=[(1, 'Nao Definido')], verbose_name='Status')),
                ('tipo_objeto', models.IntegerField(choices=[(1, 'Nao Definido')], verbose_name='Tipo de Objeto')),
                ('num_sic', models.CharField(max_length=50, verbose_name='Número no Sistema Contratos')),
                ('tipo_modalidade_aquisicao', models.IntegerField(choices=[(0, 'Nao informado'), (1, 'Licitacao'), (2, 'Dispensa'), (3, 'Inexigibilidade')], verbose_name='Tipo da Modalidade de Aquisição')),
                ('valor_original', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Original')),
                ('valor_contrapartida', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor da Contra-Partida')),
                ('data_assinatura', models.DateTimeField(verbose_name='Data de Assinatura')),
                ('data_publicacao', models.DateTimeField(verbose_name='Data de Publicação')),
                ('num_pagina_diario_oficial', models.IntegerField(verbose_name='Página do Diário Oficial')),
                ('data_publicacao_portal', models.DateTimeField(verbose_name='Data de Publicação no Portal')),
                ('data_inicio', models.DateTimeField(verbose_name='Data de Início')),
                ('vigencia', models.IntegerField(verbose_name='Vigência')),
                ('data_termino', models.DateTimeField(verbose_name='Data de Término')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('conta_controle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_conta_controle', to='controle.contascontrole')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontrato_created_by', to=settings.AUTH_USER_MODEL)),
                ('credor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_credor', to='execucao_orcamentaria.credores')),
                ('dispensa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_dispensa', to='dispositivos_de_contratacao.dispensas')),
                ('dispositivo_legal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_dispositivo_legal', to='cadastros_basicos.dispositivoslegais')),
                ('inexigibilidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_inexigibilidade', to='dispositivos_de_contratacao.inexigibilidades')),
                ('licitacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontrato_licitacao', to='dispositivos_de_contratacao.licitacoes')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontrato_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Despesa sem Contrato',
                'verbose_name_plural': 'Despesas sem Contrato',
            },
        ),
        migrations.CreateModel(
            name='DespesasSemContratoDotacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratodotacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('despesas_sem_contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratodotacoes_despesas_sem_contrato', to='despesas_sem_contrato.despesassemcontrato')),
                ('dotacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratodotacoes_dotacao', to='planejamento.orcamentosdespesas')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratodotacoes_orcamento', to='planejamento.orcamentos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratodotacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dotação da Despesa sem Contrato',
                'verbose_name_plural': 'Dotações de Despesas sem Contrato',
            },
        ),
        migrations.CreateModel(
            name='DespesasSemContratoCronogramaMensal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('valor_jan', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Janeiro')),
                ('valor_fev', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Fevereiro')),
                ('valor_mar', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Março')),
                ('valor_abr', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Abril')),
                ('valor_mai', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Maio')),
                ('valor_jun', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Junho')),
                ('valor_jul', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Julho')),
                ('valor_ago', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Agosto')),
                ('valor_set', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Setembro')),
                ('valor_out', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Outubro')),
                ('valor_nov', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Novembro')),
                ('valor_dez', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de Dezembro')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratocronogramamensal_created_by', to=settings.AUTH_USER_MODEL)),
                ('despesas_sem_contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratocronogramamensal_despesas_sem_contrato', to='despesas_sem_contrato.despesassemcontrato')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratocronogramamensal_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cronograma Mensal da Despesa sem Contrato',
                'verbose_name_plural': 'Cronogramas Mensais de Despesas Sem Contrato',
            },
        ),
        migrations.CreateModel(
            name='DespesasSemContratoArquivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('nome_arquivo', models.CharField(max_length=500, verbose_name='Nome do Arquivo')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratoarquivos_created_by', to=settings.AUTH_USER_MODEL)),
                ('despesas_sem_contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratoarquivos_despesas_sem_contrato', to='despesas_sem_contrato.despesassemcontrato')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='despesassemcontratoarquivos_tipo', to='cadastros_basicos.arquivostipos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despesassemcontratoarquivos_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Arquivo da Despesa sem Contrato',
                'verbose_name_plural': 'Arquivos de Despesas sem Contrato',
            },
        ),
    ]