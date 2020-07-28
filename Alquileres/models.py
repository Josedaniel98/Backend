  
#Modelo de Alquileres de Maquinaria

#Modelo Owner que me servirá para todos los modelos/asignar propietario de alquiler
from django.db import models
#Esta importación es para tomar el ID del usuario para relacionarlo con el QueryKey
from django.conf import settings

class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class Alquiler(OwnerModel):
    fecha_inicio = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    maquinaria = models.ForeignKey('maquinaria.Maquinaria', on_delete = models.CASCADE, related_name = 'maquinaria')
    total = models.FloatField()
    def __str__(self):
        return '{} {}'.format(self.maquinaria, self.total)
    
