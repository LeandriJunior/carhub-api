# Generated by Django 4.2.7 on 2024-02-04 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('automovel', '0001_initial'),
        ('usuario', '0002_alter_usuario_user'),
        ('ordem_servico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='carro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='automovel.automovel'),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.usuario'),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='dt_entrega',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='dt_expedicao',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='hr_expedicao',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario'),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='status_ordem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ordem_servico.ordemservicostatus'),
        ),
    ]