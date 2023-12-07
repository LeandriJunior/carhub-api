# Generated by Django 4.2.7 on 2023-12-07 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaginaConfiguracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, null=True)),
                ('dt_criacao', models.DateTimeField(null=True)),
                ('dt_edicao', models.DateTimeField(null=True)),
                ('user_criacao', models.CharField(max_length=255, null=True)),
                ('user_edicao', models.CharField(max_length=255, null=True)),
                ('background_color', models.CharField(max_length=6)),
                ('background_image', models.CharField(max_length=1024, null=True)),
                ('logo', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'db_table': 'sistema_pagina_configuracao',
            },
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, null=True)),
                ('dt_criacao', models.DateTimeField(null=True)),
                ('dt_edicao', models.DateTimeField(null=True)),
                ('user_criacao', models.CharField(max_length=255, null=True)),
                ('user_edicao', models.CharField(max_length=255, null=True)),
                ('nome', models.CharField(max_length=255, null=True)),
                ('principal', models.BooleanField(null=True)),
                ('configuracao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pagina.paginaconfiguracao')),
                ('pagina_pai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pagina.pagina')),
            ],
            options={
                'db_table': 'sistema_pagina',
            },
        ),
    ]
