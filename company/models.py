from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import *
from django.utils import timezone
from simple_history.models import HistoricalRecords

# Create your models here.


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
    Company Model
    '''

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    register_steps = models.IntegerField(
        _('Pasos de creacion de cuenta'), default=0)
    is_active = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _('Fecha creación'), default=timezone.now)

    legal_business_name = models.CharField(_('Instutución'), max_length=150)
    commercial_name = models.CharField(
        _('Nombre comercial de la Instutución'), max_length=150)

    nit = models.CharField(_('Nit'), max_length=30, null=False, unique=True)
    dpi = models.CharField(_('DPI'), max_length=30, null=False, unique=True)
    phone = models.CharField(_('Teléfono'), max_length=15, null=False)
    website = models.CharField(_('Página web'), max_length=25, default='')
    address = models.CharField(_('Dirección'), max_length=250)
    description = models.CharField(_('Descripción'), max_length=700, null=True)

    # historial de cambios
    history = HistoricalRecords(verbose_name=_("Historial"))

    def __str__(self):
        return self.legal_business_name
