from django.db import models

# Create your models here.
class Maquinaria (models.Model):
    PESADA = 1
    LIVIANA = 3
    HERRAMIENTA = 5
    #
    DISPONIBLE = 1
    NO_DISPONIBLE = 0
    
    TIPOS = (
        (PESADA, 'Maquinaria Pesada'),
        (LIVIANA, 'Maquinaria Liviana'),
        (HERRAMIENTA, 'Herramienta de mano')
    )
    
    ESTADO = (
        (DISPONIBLE, 'Disponible'),
        (NO_DISPONIBLE, 'No Disponible')
    )
    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.SmallIntegerField(choices = ESTADO, default = DISPONIBLE)
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.descripcion)

