from django.db import models

import core.models


# Create your models here.

class Empresa(core.models.Log):
    logo = models.CharField(max_length=2048, null=True, default='empresa/logo/sem-logo.png')
    cor_principal = models.CharField(max_length=10, null=True)
    cor_secundaria = models.CharField(max_length=10, null=True)
    nome = models.CharField(max_length=255, null=True)


class ModuloEmpresa(core.models.Log):
    nome = models.CharField(max_length=255, null=True)
    acesso = models.BooleanField(default=True)

