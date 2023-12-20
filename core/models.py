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

class ContatoLog(models.Model):
    celular_numero = models.CharField(max_length=50, null=True)
    celular_ddd = models.CharField(max_length=3, null=True)
    celular_completo = models.CharField(max_length=50, null=True)
    celular_completo_form = models.CharField(max_length=50, null=True)

    telefone_numero = models.CharField(max_length=50, null=True)
    telefone_ddd = models.CharField(max_length=3, null=True)
    telefone_completo = models.CharField(max_length=50, null=True)
    telefone_completo_form = models.CharField(max_length=50, null=True)

    email = models.EmailField(max_length=200, null=True)
    email_financeiro = models.EmailField(max_length=200, null=True)
    email_documentacao = models.EmailField(max_length=200, null=True)

    class Meta():
        abstract = True


class PessoaLog(ContatoLog):
    nm_completo = models.CharField(max_length=200, null=True)
    nm_primeiro = models.CharField(max_length=200, null=True)
    nm_ultimo = models.CharField(max_length=200, null=True)

    cpf = models.BigIntegerField(null=True)
    cpf_form = models.CharField(max_length=20, null=True)

    rg = models.CharField(max_length=15, null=True)
    rg_form = models.CharField(max_length=15, null=True)

    dat_nasc = models.DateField(null=True)

    imagem = models.FileField(upload_to='fotos/usuarios', default='fotos/sem-foto.png', null=True)

    SEXOS = (
        ("masculino", "Masculino"),
        ("femenino", "Femenino"),
        ("outros", "Outros")
    )

    sexo = models.CharField(max_length=9, null=True, choices=SEXOS)

    class Meta():
        abstract = True


class PessoaJuridicaLog(models.Model):
    cnpj = models.CharField(max_length=50, null=True)
    cnpj_form = models.CharField(max_length=50, null=True)
    nome = models.CharField(max_length=200, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    nm_fantasia = models.CharField(max_length=200, null=True)

    class Meta():
        abstract = True



