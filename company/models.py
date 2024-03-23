from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import *

# Create your models here.
class Role(models.Model):
    """
    Modelo para roles de empresas (ej. Doctor, Enfemera)
    """
    objects = RoleManager()
    name = models.CharField(_('Nombre'), max_length=50)
    name_spanish = models.CharField(_('Nombre Español'), max_length=50, default='')
    description = models.CharField(_('Descripción'), max_length=150)
    def __str__(self):
        return self.name
