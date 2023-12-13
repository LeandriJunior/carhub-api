import datetime

from django.db import models


# Create your models here.

class Log(models.Model):
    status = models.BooleanField(default=True, null=True)
    dt_criacao = models.DateTimeField(null=True)
    dt_edicao = models.DateTimeField(null=True)
    user_criacao = models.CharField(max_length=255, null=True)
    user_edicao = models.CharField(max_length=255, null=True)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.dt_criacao = datetime.datetime.now()
            try:
                self.user_criacao = self.request.user.pk
            except:
                pass
        self.dt_edicao = datetime.datetime.now()
        try:
            self.user_edicao = self.request.user.pk
        except:
            pass

        return super(Log, self).save(*args, **kwargs)


class EnderecoLog(models.Model):
    """
    :Nome da classe/função: EnderecoLog
    :descrição: Classe abstrata que é usada como pai para classes que irão ter informações de endereço
    :Criação: Nícolas Marinoni Grande - 17/08/2020
    :Edições:
    """
    cep = models.CharField(max_length=10, null=True)
    cep_form = models.CharField(max_length=15, null=True)
    municipio = models.CharField(max_length=15, null=True)
    bairro_cep = models.CharField(max_length=100, null=True)
    endereco_cep = models.CharField(max_length=100, null=True)
    endereco_comp_cep = models.CharField(max_length=200, null=True)
    latitude_cep = models.CharField(max_length=200, null=True)
    longitude_cep = models.CharField(max_length=200, null=True)
    tipo_cep = models.CharField(max_length=200, null=True)

    class Meta():
        abstract = True


class EmpresaLog(models.Model):
    nome = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=50, null=True)
    cnpj_form = models.CharField(max_length=50, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    nm_fantasia = models.CharField(max_length=200, null=True)

    class Meta():
        abstract = True
