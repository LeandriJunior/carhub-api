# Generated by Django 4.2.7 on 2023-11-21 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('status', models.BooleanField(default=True, null=True)),
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nm_descritivo', models.CharField(max_length=512, null=True)),
                ('descricao', models.CharField(max_length=1024, null=True)),
                ('modulo', models.CharField(max_length=64, null=True)),
                ('prioridade', models.IntegerField(null=True)),
                ('grupo_pai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='permissao.grupo')),
            ],
            options={
                'db_table': 'sistema_grupo',
            },
        ),
        migrations.CreateModel(
            name='PontoFuncao',
            fields=[
                ('status', models.BooleanField(default=True, null=True)),
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nm_descritivo', models.CharField(max_length=512, null=True)),
                ('descricao', models.CharField(max_length=1024, null=True)),
                ('modulo', models.CharField(max_length=64, null=True)),
                ('prioridade', models.IntegerField(null=True)),
                ('ponto_funcao_pai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='permissao.pontofuncao')),
            ],
            options={
                'db_table': 'sistema_pontofuncao',
            },
        ),
        migrations.CreateModel(
            name='GrupoPontoFuncao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, null=True)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='permissao.grupo')),
                ('ponto_funcao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='permissao.pontofuncao')),
            ],
            options={
                'db_table': 'sistema_grupo_pontofuncao',
            },
        ),
    ]
