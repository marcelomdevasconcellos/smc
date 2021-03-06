# Generated by Django 3.2 on 2022-03-26 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros_basicos', '0001_initial'),
        ('execucao_orcamentaria', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planejamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispensas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('numero', models.CharField(max_length=10, verbose_name='Número da Dispensa')),
                ('num_processo', models.CharField(max_length=10, verbose_name='Número do Processo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('data_publicacao', models.DateField(verbose_name='Data de Publicação')),
                ('num_pagina_diario_oficial', models.DateField(verbose_name='Número da Página no D.O.')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dispensas_created_by', to=settings.AUTH_USER_MODEL)),
                ('credor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispensas_credor', to='execucao_orcamentaria.credores')),
                ('dispositivo_legal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispensas_dispositivo_legal', to='cadastros_basicos.dispositivoslegais')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dispensas_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dispensa',
                'verbose_name_plural': 'Dispensas',
            },
        ),
        migrations.CreateModel(
            name='Inexigibilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('numero', models.CharField(max_length=10, verbose_name='Número da Dispensa')),
                ('num_processo', models.CharField(max_length=10, verbose_name='Número do Processo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('arquivo', models.CharField(max_length=255, verbose_name='Arquivo')),
                ('data_publicacao', models.DateField(verbose_name='Data de Publicação')),
                ('num_pagina_diario_oficial', models.DateField(verbose_name='Número da Página no D.O.')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inexigibilidades_created_by', to=settings.AUTH_USER_MODEL)),
                ('credor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inexigibilidades_credor', to='execucao_orcamentaria.credores')),
                ('dispositivo_legal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inexigibilidades_dispositivo_legal', to='cadastros_basicos.dispositivoslegais')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inexigibilidades_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inexigibilidade',
                'verbose_name_plural': 'Inexigibilidades',
            },
        ),
        migrations.CreateModel(
            name='Licitacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('nome_orgao_ata', models.CharField(max_length=200, verbose_name='Nome do Órgão')),
                ('cpf_gestor', models.CharField(max_length=11, verbose_name='CPF do Gestor')),
                ('numero_licitacao', models.CharField(choices=[('1', 'Nao Definido')], max_length=20, verbose_name='Número da Licitação')),
                ('tipo_licitacao', models.IntegerField(verbose_name='Tipo de Licitação')),
                ('modalidade_licitacao', models.CharField(max_length=20, verbose_name='Modalidade da Licitação')),
                ('modalidade_processo_administrativo', models.CharField(max_length=20, verbose_name='Modalidade do Processo Administrativo')),
                ('descricao1_motivo_fornecedor', models.TextField(verbose_name='Descrição do Motivo do Fornecedor')),
                ('descricao2_motivo_fornecedor', models.TextField(verbose_name='Descrição do Motivo do Fornecedor')),
                ('descricao1_objeto_licitacao', models.TextField(verbose_name='Descrição do Objeto da Licitação')),
                ('descricao2_objeto_licitacao', models.TextField(verbose_name='Descrição do Objeto da Licitação')),
                ('descricao1_justificativa_preco', models.TextField(verbose_name='Descrição/Justificativa de Preço')),
                ('descricao2_justificativa_preco', models.TextField(verbose_name='Descrição/Justificativa de Preço')),
                ('nome_responsavel_juridico', models.CharField(max_length=200, verbose_name='Nome do Responsável Jurídico')),
                ('cpf_responsavel_juridico', models.CharField(max_length=11, verbose_name='CPF do Responsável Jurídico')),
                ('nome_responsavel_homologacao', models.CharField(max_length=200, verbose_name='Nome do Responsável pela Homologação')),
                ('cpf_responsavel_homologacao', models.CharField(max_length=11, verbose_name='CPF do Responsável pela Homologação')),
                ('numero_comissao', models.CharField(max_length=20, verbose_name='Número da Comissão')),
                ('data_criacao_comissao', models.DateField(verbose_name='Data de Criação da Comissão')),
                ('data_emissao_edital', models.DateField(verbose_name='Data de Emissão do Edital')),
                ('data_homologacao', models.DateField(verbose_name='Data de Homologação')),
                ('data_realizacao_autuacao_licitacao', models.DateField(verbose_name='Data de Realização da Autuação da Licitação')),
                ('data_realizacao_licitacao', models.DateField(verbose_name='Data de Realização da Licitação')),
                ('hora_licitacao', models.CharField(max_length=20, verbose_name='Hora de Realização da Licitação')),
                ('valor_limite_superior', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do Limite Superior')),
                ('valor_orcado_estimado', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor Orçado Estimado')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='licitacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='licitacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Licitação',
                'verbose_name_plural': 'Licitações',
            },
        ),
        migrations.CreateModel(
            name='LicitacoesDotacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='licitacoesdotacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('licitacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='licitacoesdotacoes_licitacao', to='dispositivos_de_contratacao.licitacoes')),
                ('orcamento_despesa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='licitacoesdotacoes_orcamento_despesa', to='planejamento.orcamentosdespesas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='licitacoesdotacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dotação da Licitação',
                'verbose_name_plural': 'Dotações da Licitação',
            },
        ),
        migrations.CreateModel(
            name='InexigibilidadesDotacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inexigibilidadesdotacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('inexigibilidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inexigibilidadesdotacoes_inexigibilidade', to='dispositivos_de_contratacao.inexigibilidades')),
                ('orcamento_despesa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inexigibilidadesdotacoes_orcamento_despesa', to='planejamento.orcamentosdespesas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inexigibilidadesdotacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dotação da Inexigibilidade',
                'verbose_name_plural': 'Dotações da Inexigibilidade',
            },
        ),
        migrations.CreateModel(
            name='DispensasDotacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dispensasdotacoes_created_by', to=settings.AUTH_USER_MODEL)),
                ('dispensa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispensasdotacoes_dispensa', to='dispositivos_de_contratacao.dispensas')),
                ('orcamento_despesa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispensasdotacoes_orcamento_despesa', to='planejamento.orcamentosdespesas')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dispensasdotacoes_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dotação da Dispensa',
                'verbose_name_plural': 'Dotações da Dispensa',
            },
        ),
    ]
