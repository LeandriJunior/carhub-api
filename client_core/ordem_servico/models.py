from django.db import models

from core.models import Log


# Create your models here.

class OrdemServico(Log):
    cliente = models.ForeignKey('cliente.Usuario', on_delete=models.DO_NOTHING, null=True)
    carro = models.ForeignKey('automovel.Automovel', on_delete=models.DO_NOTHING, null=True)
    status_ordem = models.ForeignKey('OrdemServicoStatus', on_delete=models.DO_NOTHING, null=True)
    is_aprovado = models.BooleanField(default=False),
    dt_expedicao = models.DateField(null=True)
    hr_expedicao = models.DateField(null=True)
    dt_entrega = models.CharField(max_length=5, null=True)
    hr_entrega = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = f'ordemservico'


class OrdemServicoStatus(Log):
    nome = models.CharField(max_length=255, primary_key=True)
    ordem = models.IntegerField(null=True)
    responsavel = models.ForeignKey('usuario.Usuario', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = f'ordemservico_status'


class OrdemServicoStatusLog(Log):
    status_ordem = models.ForeignKey('OrdemServicoStatus', on_delete=models.DO_NOTHING, null=True)
    ordem = models.ForeignKey('OrdemServico', on_delete=models.DO_NOTHING, null=True)
    ordem = models.IntegerField(null=True)

    class Meta:
        db_table = f'ordemservico_status_log'
