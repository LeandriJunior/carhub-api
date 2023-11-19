from django.db import models

import core.models


# Create your models here.

class Usuario(core.models.Log):
    nome = models.CharField(max_length=255, null=True)
    idade = models.IntegerField(null=True)
    is_client = models.BooleanField()