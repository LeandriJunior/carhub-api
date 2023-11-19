from django.db import models
from tenant_schemas.models import TenantMixin
import core.models


# Create your models here.

class Client(TenantMixin, core.models.Log):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True