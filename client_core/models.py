from django.db import models

import core.models


# Create your models here.

class Tipo(core.models.Log):
    codigo = models.CharField(max_length=200, primary_key=True)
    informacao = models.CharField(max_length=500, null=True)
    tipo = models.CharField(max_length=200, null=True)
    nome = models.CharField(max_length=200, null=True)
    descricao = models.TextField(null=True)
    ordem = models.IntegerField(null=True)

    class Meta:
        db_table = "tipo"