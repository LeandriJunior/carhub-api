from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
import core.models


# Create your models here.




class Profile(AbstractBaseUser, core.models.Log, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(null=True, default=False)
    is_atualizar_sessao = models.BooleanField(default=False, null=True)
    is_primeiro_login = models.BooleanField(default=True, null=True)
    is_resetar_senha = models.BooleanField(default=False, null=True)
    senha_padrao = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )

    class Meta:
        abstract = True


class UsuarioLogin(Profile):
    nm_primeiro = models.CharField(max_length=200, null=True)
    nm_ultimo = models.CharField(max_length=200, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'usuario_login'


class Usuario(core.models.Log):
    user = models.ForeignKey('UsuarioLogin', on_delete=models.DO_NOTHING, null=True)
    nm_completo = models.CharField(max_length=255, null=True)
    idade = models.IntegerField(null=True)
    is_client = models.BooleanField()
    tela_principal = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = 'usuario'
