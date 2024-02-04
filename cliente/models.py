from django.db import models
from core.models import Log, EnderecoLog, PessoaLog


class Usuario(Log, EnderecoLog, PessoaLog):
    tela_principal = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cliente'
