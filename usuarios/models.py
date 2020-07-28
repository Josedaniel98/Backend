from django.db import models
from django.contrib.auth.models import AbstractUser

class usuario (AbstractUser):
    username = models.CharField(
        'username',
        unique = True,
        max_length = 50,
        error_messages = {
            'unique': 'Ya existe un usuario con este nombre.'
        }
    )

    # USERNAME_FIELD = ''

    email = models.EmailField(
        'email_address',
        unique = True,
        error_messages = {
            'unique': 'Ya existe un usuario con este correo.'
        }
    )

    is_staff = models.BooleanField(
        'administrador',
        default = False,
        help_text = 'Verdadero cuando el usuario es administrador.'
    )

    is_active = models.BooleanField(
        'usuario_activo',
        default = True
    )

    #is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
