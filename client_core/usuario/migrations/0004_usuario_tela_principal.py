# Generated by Django 4.2.7 on 2023-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_dt_criacao_usuario_dt_edicao_usuario_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tela_principal',
            field=models.CharField(max_length=255, null=True),
        ),
    ]