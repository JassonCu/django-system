from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
    Manejador de usuarios que permite el control en creacion, edicion y obtencion de usuarios y roles
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserCompanyAssetManager(models.Manager):
    """
    Manejador de assets que permite el control en creacion, edicion y obtencion
    """

    def get_assets(self):
        return self.get_queryset()

    def create_asset(self, tx_id,  user, company, is_admin, is_developer, **extra_fields):
        extra_fields.setdefault('tx_id', tx_id)
        extra_fields.setdefault('user', user)
        if is_developer:
            extra_fields.setdefault('is_admin', False)
            extra_fields.setdefault('is_developer', True)
        else:
            extra_fields.setdefault('is_admin', is_admin)
        extra_fields.setdefault('company', company)
        asset = self.model(**extra_fields)
        asset.save()
        return asset
