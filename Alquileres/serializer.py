#Serializador para Alquileres
from rest_framework import serializers
from maquinaria.serializers import MaquinariaSerializer
#Modelo
from .models import Alquiler

class AlquilerSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault()) #Valor que provee Django RF para obtener el valor del usuario logueado
    # estado = serializers.SerializerMethodField(read_only=True)
    # estado = MaquinariaSerializer(read_only = True, many=True)
    
    class Meta:
        model = Alquiler
        fields = ('owner','fecha_inicio', 'fecha_devolucion', 'total', 'maquinaria','estado')
        
    # def get_estado(self, obj):
    #     return MaquinariaSerializer(obj.maquinaria).data
    
    # def create(self, validated_data):
    #     if estado.estado == 1:
    #         pass