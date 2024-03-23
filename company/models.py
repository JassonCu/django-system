from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from .managers import *


class Role(models.Model):
    """
    Modelo para roles de empresas (ej. Doctor, Enfemera)
    """
    objects = RoleManager()
    name = models.CharField(_('Nombre'), max_length=50)
    name_spanish = models.CharField(
        _('Nombre Español'), max_length=50, default='')
    description = models.CharField(_('Descripción'), max_length=150)

    def __str__(self):
        return self.name


class Company(models.Model):
    '''
    Company model.
    '''

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    register_steps = models.IntegerField(
        _('Pasos de creacion de cuenta'), default=0)
    is_active = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    collaborator_can_create_invoice = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _('Fecha creación'), default=timezone.now)

    legal_business_name = models.CharField(_('Razón social'), max_length=150)
    commercial_name = models.CharField(_('Nombre comercial'), max_length=150)

    nit = models.CharField(_('Nit'), max_length=30, null=False, unique=True)
    phone = models.CharField(_('Teléfono'), max_length=15, null=False)
    website = models.CharField(_('Página web'), max_length=25, default='')
    address = models.CharField(_('Dirección'), max_length=250)
    description = models.CharField(_('Descripción'), max_length=700, null=True)

    # historial de cambios
    history = HistoricalRecords(verbose_name=_("Historial"))

    def __str__(self):
        return self.legal_business_name

    def is_valid(self):
        return not self.is_blocked and self.is_active
