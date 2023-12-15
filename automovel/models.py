from django.db import models

from core.models import Log


# Create your models here.

class Automovel(Log):
    modelo = models.ForeignKey('Modelo', on_delete=models.DO_NOTHING, null=True)
    placa = models.CharField(max_length=7, null=False)
    placa_form = models.CharField(max_length=8, null=True)
    cor = models.ForeignKey('core.Tipo', on_delete=models.DO_NOTHING, null=True, related_name='cor')
    quilometragem = models.IntegerField(null=True)
    proprietario = models.ForeignKey('cliente.Usuario', on_delete=models.DO_NOTHING, null=True)
    observacoes = models.CharField(max_length=1024, null=True)

    class Meta:
        db_table = 'automovel'


class Modelo(Log):
    modelo = models.CharField(max_length=32, null=True)
    marca = models.ForeignKey('Marca', on_delete=models.DO_NOTHING, null=True)
    ano_lancamento = models.DateField(null=True)
    tipo_motor = models.ForeignKey('core.Tipo', on_delete=models.DO_NOTHING, null=True, related_name='motor')
    potencia_motor = models.IntegerField(null=True)
    combustivel = models.ForeignKey('core.Tipo', on_delete=models.DO_NOTHING, null=True, related_name='combustivel')
    transmissao = models.ForeignKey('core.Tipo', on_delete=models.DO_NOTHING, null=True, related_name='transmissao')
    nm_portas = models.ForeignKey('core.Tipo', on_delete=models.DO_NOTHING, null=True, related_name='portas')
    chassis = models.IntegerField(null=True)
    class Meta:
        db_table = 'automovel_modelo'


class Marca(Log):
    marca = models.CharField(max_length=32, null=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'automovel_marca'