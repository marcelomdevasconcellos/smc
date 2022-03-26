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
            name='Convenios',
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
                ('concluido_divida', models.BooleanField(verbose_name='Concluído com dívida?')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenios_created_by', to=settings.AUTH_USER_MODEL)),
                ('credor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenios_credor', to='execucao_orcamentaria.credores')),
                ('dispensa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenios_dispensa', to='dispositivos_de_contratacao.dispensas')),
                ('dispositivo_legal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenios_dispositivo_legal', to='cadastros_basicos.dispositivoslegais')),
                ('inexigibilidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenios_inexigibilidade', to='dispositivos_de_contratacao.inexigibilidades')),
                ('licitacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenios_licitacao', to='dispositivos_de_contratacao.licitacoes')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenios_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Convênio',
                'verbose_name_plural': 'Convênios',
            },
        ),
        migrations.CreateModel(
            name='ConveniosDotacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosdotacoes_convenio', to='convenios.convenios')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosdotacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('dotacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosdotacoes_dotacao', to='planejamento.orcamentosdespesas')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosdotacoes_orcamento', to='planejamento.orcamentos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosdotacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dotação do Convênio',
                'verbose_name_plural': 'Dotações do Convênio',
            },
        ),
        migrations.CreateModel(
            name='ConveniosCronogramaMensal',
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
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenioscronogramamensal_convenio', to='convenios.convenios')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenioscronogramamensal_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenioscronogramamensal_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cronograma Mensal do Convênio',
                'verbose_name_plural': 'Cronogramas Mensais do Convênio',
            },
        ),
        migrations.CreateModel(
            name='ConveniosContasControle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('conta_controle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenioscontascontrole_conta_controle', to='controle.contascontrole')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='convenioscontascontrole_convenio', to='convenios.convenios')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenioscontascontrole_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='convenioscontascontrole_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vinculação do Convênio à Conta de Controle',
                'verbose_name_plural': 'Vinculação dos Convênios às Contas de Controle',
            },
        ),
        migrations.CreateModel(
            name='ConveniosArquivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('nome_arquivo', models.CharField(max_length=500, verbose_name='Nome do Arquivo')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosarquivos_convenio', to='convenios.convenios')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosarquivos_created_by', to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosarquivos_tipo', to='cadastros_basicos.arquivostipos')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosarquivos_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Arquivo do Convênio',
                'verbose_name_plural': 'Arquivos do Convênio',
            },
        ),
        migrations.CreateModel(
            name='ConveniosAditivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('data_assinatura', models.DateTimeField(verbose_name='Data de Assinatura')),
                ('data_publicacao', models.DateTimeField(verbose_name='Data de Publicação')),
                ('num_pagina_diario_oficial', models.IntegerField(verbose_name='Página do Diário Oficial')),
                ('data_inicio', models.DateTimeField(verbose_name='Data de Início')),
                ('vigencia', models.IntegerField(verbose_name='Vigência')),
                ('data_termino', models.DateTimeField(verbose_name='Data de Término')),
                ('num_documento', models.CharField(max_length=50, verbose_name='Número do Documento')),
                ('objeto', models.CharField(max_length=500, verbose_name='Objeto')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('valor_contrapartida', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor da Contra-Partida')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conveniosaditivos_convenio', to='convenios.convenios')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosaditivos_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conveniosaditivos_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aditivo do Convênio',
                'verbose_name_plural': 'Aditivos do Convênio',
            },
        ),
    ]