from django.db import models


class RoleManager(models.Manager):
    """
    Manejador de roles de empresas que permite el control en creacion, edicion y obtencion
    """

    def get_groups(self):
        return self.get_queryset()
