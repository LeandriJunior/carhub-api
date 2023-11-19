from django.db import models


# Create your models here.

class Log(models.Model):
    status = models.BooleanField(default=True, null=True)

    class Meta:
        abstract = True
