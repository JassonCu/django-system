from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    """
    User model which extends Django's user model
    """

    username = None
    first_name = None
    last_name = None

    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(
        _('Nombre'), max_length=150, blank=True, default='')
    token_email_validation = models.CharField(
        _('Token para validar correo'), max_length=100, blank=False, default='')
    token_password_reset = models.CharField(
        _('Token para reiniciar password'), max_length=100, blank=False, default='')
    token_expiration = models.DateTimeField(
        _('Fecha valida para token'), null=True)
    public_key = models.CharField(
        _('Public key'), max_length=100, blank=False, default='')
    private_key = models.CharField(
        _('Private key'), max_length=100, blank=False, default='')
    two_factor_auth_key = models.CharField(
        _('2do Factor de Autenticación Key'), max_length=16, default='')
    phone_number = models.CharField(
        _('Número de teléfono'), max_length=25, blank=False, default='')
    two_factor_auth_method = models.IntegerField(
        _('Metodo 2do Factor de Autenticación'), default=0)
    receive_emails = models.BooleanField(
        _('Recibir correos electrónicos'), default=True)
    groups = models.ManyToManyField(Group, verbose_name=_(
        'Grupos'), related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_(
        'Permisos de Usuario'), related_name='custom_user_permissions')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects: UserManager = UserManager()

    def __str__(self):
        return self.full_name
