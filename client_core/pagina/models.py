from django.db import models

from core.models import Log


# Create your models here.

class Pagina(Log):
    nome = models.CharField(max_length=255, null=True)
    principal = models.BooleanField(null=True)
    pagina_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    configuracao = models.ForeignKey('PaginaConfiguracao', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'sistema_pagina'


class PaginaConfiguracao(Log):
    background_color = models.CharField(max_length=6, null=False)
    background_image = models.CharField(max_length=1024, null=True)
    logo = models.CharField(max_length=1024, null=True)
    configuracao = models.TextField(null=True)

    class Meta:
        db_table = 'sistema_pagina_configuracao'
