from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    # Agrega related_name para evitar conflictos
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    objects: UserManager = UserManager()