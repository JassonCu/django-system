# Generated by Django 5.0.1 on 2024-03-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='two_factor_auth_key',
            field=models.CharField(default='', max_length=16, verbose_name='2do Factor de Autenticación Key'),
        ),
        migrations.AddField(
            model_name='user',
            name='two_factor_auth_method',
            field=models.IntegerField(default=0, verbose_name='Metodo 2do Factor de Autenticación'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='custom_user_groups', to='auth.group', verbose_name='Grupos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='custom_user_permissions', to='auth.permission', verbose_name='Permisos de Usuario'),
        ),
    ]
