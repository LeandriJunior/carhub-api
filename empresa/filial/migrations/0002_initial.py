# Generated by Django 4.2.7 on 2024-02-02 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('filial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filial',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario'),
        ),
    ]
