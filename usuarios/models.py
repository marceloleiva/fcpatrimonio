#encoding:utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils import timezone

GENERO = (
    ('M', 'Hombre'),
    ('F', 'Mujer'),
)

NOW = timezone.now()


class PerfilUsuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length=40, unique=True, db_index=True)
    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    rut = models.CharField('RUT', max_length=10, unique=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO, blank=True)
    celular = models.PositiveIntegerField('Celular', max_length=10, null=True)
    imei = models.CharField('IMEI', max_length=30, blank=True)
    date_joined = models.DateTimeField('Fecha ingreso', default=NOW)
    date_of_birth = models.DateField('Fecha nacimiento', null=True)
    is_active = models.BooleanField('Puede iniciar sesión? ', default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'rut']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return '%s , %s' % self.first_name, self.apellidos

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.first_name

    def __unicode__(self):
        return self.last_name

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True
