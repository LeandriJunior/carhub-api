# Generated by Django 4.2.7 on 2024-02-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('status', models.BooleanField(default=True, null=True)),
                ('dt_criacao', models.DateTimeField(null=True)),
                ('dt_edicao', models.DateTimeField(null=True)),
                ('user_criacao', models.CharField(max_length=255, null=True)),
                ('user_edicao', models.CharField(max_length=255, null=True)),
                ('codigo', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('informacao', models.CharField(max_length=500, null=True)),
                ('tipo', models.CharField(max_length=200, null=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('descricao', models.TextField(null=True)),
                ('ordem', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'tipo',
            },
        ),
    ]
