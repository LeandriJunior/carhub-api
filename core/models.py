from datetime import timezone

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
            self.dt_criacao = timezone.now()
            try:
                self.user_criacao = self.request.user.pk
            except:
                pass
        self.dt_edicao = timezone.now()
        try:
            self.user_edicao = self.request.user.pk
        except:
            pass

        return super(Log, self).save(*args, **kwargs)
