from django.db import models


class RoleManager(models.Manager):
    """
    Enterprise role manager that allows control over creation, editing, and retrieval
    """

    def get_groups(self):
        return self.get_queryset()
