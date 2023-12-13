from django.db import models

from core.models import Log, EmpresaLog, EnderecoLog


# Create your models here.

class Empresa(Log, EmpresaLog, EnderecoLog):


    class Meta:
        db_table = 'empresa'


