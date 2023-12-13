from django.db import models

from core.models import Log, EmpresaLog, EnderecoLog


# Create your models here.
class Filial(Log, EmpresaLog, EnderecoLog):
    empresa = models.ForeignKey('empresa.Empresa', on_delete=models.DO_NOTHING, null=True)
    responsavel = models.ForeignKey('usuario.Usuario', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        db_table = 'empresa_filial'
